from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.utils.timezone import now
from books.models import Book
from members.models import Member
from transactions.models import Transaction
from datetime import date

def home(request):
    query = request.GET.get('search', '')

    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__icontains=query) |
            Q(isbn__icontains=query)
        )

    # ✅ total copies
    total_books = Book.objects.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    # ✅ available copies
    available_books = Book.objects.aggregate(
        total=Sum('available_count')
    )['total'] or 0

    # ✅ correct borrowed count
    borrowed_books = Transaction.objects.filter(status='ISSUED').count()

    total_members = Member.objects.count()

    return render(request, 'home.html', {
        'books': books,
        'query': query,
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'total_members': total_members,
    })


def members_page(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})


def transactions_page(request):
    transactions = Transaction.objects.all().order_by('-issue_date')
    return render(request, 'transactions.html', {'transactions': transactions})


def issue_book(request):
    members = Member.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        member = Member.objects.get(id=request.POST.get('member'))
        book = Book.objects.get(id=request.POST.get('book'))
        due_date = request.POST.get('due_date')

        # 🔥 prevent issuing if no stock
        if book.available_count <= 0:
            return redirect('home')

        Transaction.objects.create(
            member=member,
            book=book,
            due_date=due_date
        )

        # 🔥 decrease stock
        book.available_count -= 1
        book.save()

        return redirect('home')

    return render(request, 'issue_book.html', {
        'members': members,
        'books': books
    })


def return_book(request):
    transactions = Transaction.objects.filter(status='ISSUED')

    if request.method == 'POST':
        t_id = request.POST.get('transaction')

        try:
            transaction = Transaction.objects.get(id=t_id, status='ISSUED')
        except Transaction.DoesNotExist:
            return redirect('return_book')

        today = date.today()

        transaction.return_date = today
        transaction.status = 'RETURNED'

        # 🔥 AUTO FINE CALCULATION
        if today > transaction.due_date:
            days_late = (today - transaction.due_date).days
            transaction.fine = days_late * 10
        else:
            transaction.fine = 0

        transaction.save()

        # increase stock
        book = transaction.book
        book.available_count += 1
        book.save()

        return redirect('transactions')

    return render(request, 'return_book.html', {
        'transactions': transactions
    })