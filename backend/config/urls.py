from django.contrib import admin
from django.urls import path, include
from .views import home, members_page, transactions_page, issue_book, return_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('members/', members_page, name='members'),
    path('transactions/', transactions_page, name='transactions'),
    path('issue/', issue_book, name='issue_book'),
    path('return/', return_book, name='return_book'),
    path('', home, name='home'),
]