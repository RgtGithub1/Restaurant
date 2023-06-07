from django.db import models
from django.core.validators import MinValueValidator, \
 MaxValueValidator


class Coupon(models.Model):
    code_name = models.CharField(max_length=50,
    unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
    validators=[MinValueValidator(0),
    MaxValueValidator(100)],
    help_text='Percentage value (0 to 100)')
    active = models.BooleanField()

    def __str__(self):
        return self.code_name


class EmployeeDetail(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee_role = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.employee_name
