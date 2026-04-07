from django.db import models


class Member(models.Model):
    MEMBERSHIP_STATUS = [
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('PENDING', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_id = models.CharField(max_length=20, unique=True)
    membership_status = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_STATUS,
        default='PENDING'
    )
    join_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name