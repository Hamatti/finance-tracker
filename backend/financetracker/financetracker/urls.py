from django.contrib import admin
from django.urls import path

from expenses.views import ExpenseList

urlpatterns = [
    path("api/expenses", ExpenseList.as_view()),
    path("admin/", admin.site.urls),
]
