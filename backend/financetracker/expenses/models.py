from django.db import models


class Expense(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    description = models.TextField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    store = models.CharField(max_length=200)

    def __str__(self):
        return f"<Expense> {self.description}, {self.cost}"

    def __unicode__(self):
        return f"<Expense> {self.description}, {self.cost}"

