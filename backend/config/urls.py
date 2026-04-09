from django.contrib import admin
from django.urls import path, include
from .views import home, members_page, transactions_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('members/', members_page, name='members'),
    path('transactions/', transactions_page, name='transactions'),
    path('', home, name='home'),
]