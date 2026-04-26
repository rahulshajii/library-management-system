from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from members.models import Member
from books.models import Book


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('ISSUED', 'Issued'),
        ('RETURNED', 'Returned'),
        ('OVERDUE', 'Overdue'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ISSUED'
    )

    # 🔍 VALIDATION
    def clean(self):
        # Only active members can borrow
        if self.member.membership_status != 'ACTIVE':
            raise ValidationError("Only active members can borrow books.")

        # Prevent issuing when no stock
        if self.book.available_count <= 0 and not self.pk:
            raise ValidationError("Book is currently unavailable.")

    # 🔥 CORE LOGIC
    def save(self, *args, **kwargs):
        self.full_clean()

        is_new = self.pk is None

        # 🔁 RETURN LOGIC
        if not is_new:
            old = Transaction.objects.get(pk=self.pk)

            if old.status != 'RETURNED' and self.status == 'RETURNED':
                # increase stock
                self.book.available_count += 1

                # auto fine calculation
                if self.return_date and self.return_date > self.due_date:
                    days_late = (self.return_date - self.due_date).days
                    self.fine = days_late * 10

                self.book.save()

        # 💾 SAVE TRANSACTION
        super().save(*args, **kwargs)

        # 📉 ISSUE LOGIC
        if is_new:
            self.book.available_count -= 1
            self.book.save()

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"