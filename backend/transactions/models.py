from django.db import models
from django.core.exceptions import ValidationError
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

    def clean(self):
        if self.member.membership_status != 'ACTIVE':
            raise ValidationError("Only active members can borrow books.")

        if self.book.available_count <= 0 and not self.pk:
            raise ValidationError("Book is currently unavailable.")

    def save(self, *args, **kwargs):
        self.full_clean()
        is_new = self.pk is None

        if not is_new:
            old_transaction = Transaction.objects.get(pk=self.pk)

            if (
                old_transaction.status != 'RETURNED'
                and self.status == 'RETURNED'
            ):
                self.book.available_count += 1

                if self.return_date and self.return_date > self.due_date:
                    days_late = (
                        self.return_date - self.due_date
                    ).days
                    self.fine = days_late * 10

                self.book.save()

        super().save(*args, **kwargs)

        if is_new:
            self.book.available_count -= 1
            self.book.save()

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"