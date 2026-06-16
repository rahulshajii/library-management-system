from django.contrib import admin
from django.urls import path, include
from .views import home, members_page, transactions_page, issue_book, return_book, dashboard_api

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # REST API
    path('api/books/', include('books.urls')),
    path('api/members/', include('members.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/dashboard/', dashboard_api, name='dashboard_api'),

    # Template Views
    path('', home, name='home'),
    path('members/', members_page, name='members'),
    path('transactions/', transactions_page, name='transactions'),
    path('issue/', issue_book, name='issue_book'),
    path('return/', return_book, name='return_book'),
]