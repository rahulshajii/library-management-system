from django.shortcuts import render
from django.db.models import Q, Sum
from books.models import Book
from members.models import Member
from transactions.models import Transaction


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

    total_books = Book.objects.count()
    available_books = Book.objects.aggregate(
        total=Sum('available_count')
    )['total'] or 0

    borrowed_books = total_books - available_books
    total_members = Member.objects.count()

    context = {
        'books': books,
        'query': query,
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'total_members': total_members,
    }

    return render(request, 'home.html', context)


def members_page(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def transactions_page(request):
    transactions = Transaction.objects.all().order_by('-issue_date')
    return render(
        request,
        'transactions.html',
        {'transactions': transactions}
    )