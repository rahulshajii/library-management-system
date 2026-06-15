from rest_framework import viewsets, filters
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-id')
    serializer_class = MemberSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'phone']