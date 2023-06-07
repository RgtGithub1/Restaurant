from django.db import models

from django.core.validators import MinValueValidator, \
 MaxValueValidator
# from manager.models import Coupon


class Order(models.Model):
    order_number = models.CharField(max_length=50)
    table_number = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    payment_id = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    food_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_name = models.CharField(max_length=50)
    coupon_discount = models.IntegerField()
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # address = models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=20)
    # city = models.CharField(max_length=100)
    total_food_price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # stripe_id = models.CharField(max_length=250, blank=True)
    # coupon = models.ForeignKey(Coupon,
    #                            related_name='orders',
    #                            null=True,
    #                            blank=True,
    #                            on_delete=models.SET_NULL)
    # discount = models.IntegerField(default=0,
    #                                validators=[MinValueValidator(0),
    #                                    MaxValueValidator(100)])

    # class Meta:
    #     ordering = ['-created']
    #     indexes = [
    #         models.Index(fields=['-created']),
    #     ]

    def __str__(self):
        return f'Order {self.order_number}'
