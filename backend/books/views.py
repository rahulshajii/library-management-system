from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'category', 'isbn']