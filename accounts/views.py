from rest_framework import generics
from .serializer import AccountSerializer
from .models import Account


class accountsViews(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
