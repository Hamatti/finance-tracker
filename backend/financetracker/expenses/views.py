from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer

from rest_framework import generics


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
