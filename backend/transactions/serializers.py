from rest_framework import serializers
from .models import Transaction
from members.models import Member
from books.models import Book


class TransactionSerializer(serializers.ModelSerializer):

    member_name = serializers.CharField(
        source='member.name',
        read_only=True
    )

    book_title = serializers.CharField(
        source='book.title',
        read_only=True
    )

    member = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all()
    )

    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = Transaction
        fields = [
            'id',
            'member',
            'member_name',
            'book',
            'book_title',
            'issue_date',
            'due_date',
            'return_date',
            'fine',
            'status',
        ]
