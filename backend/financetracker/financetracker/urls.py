from django.contrib import admin
from django.urls import path


from expenses.views import ExpenseList, ExpenseDetail, ExpenseCreate

urlpatterns = [
    path("api/expenses", ExpenseList.as_view()),
    path(r"api/expenses/<int:expense_id>", ExpenseDetail.as_view()),
    path(r"api/expenses/new", ExpenseCreate.as_view()),
    path("admin/", admin.site.urls),
]
