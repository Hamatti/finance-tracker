from django.shortcuts import get_object_or_404
from .models import Expense
from .serializers import ExpenseSerializer

from rest_framework import generics
from rest_framework.response import Response


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveAPIView):
    serializer_class = ExpenseSerializer

    def retrieve(self, request, expense_id, **kwargs):
        expense = get_object_or_404(Expense, id=expense_id)

        return Response(ExpenseSerializer(expense).data)


class ExpenseCreate(generics.CreateAPIView):
    serializer_class = ExpenseSerializer

    def create(self, request, **kwargs):
        ## FIXME: Add validation.
        new_expense = Expense.objects.create(**request.data)
        return Response(ExpenseSerializer(new_expense).data)
