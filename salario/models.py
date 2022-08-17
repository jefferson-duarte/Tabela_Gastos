from django.db import models


class Salario(models.Model):
    data = models.DateField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
