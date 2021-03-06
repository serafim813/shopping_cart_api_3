from django.db import models
from shopping_cart_api.products.models import Product, Category


class Campaign(models.Model):
    name = models.CharField(max_length=255, null=False)
    discount_type = models.CharField(max_length=6, choices=(('Amount', 'amount'), ('Rate', 'rate')), default="rate", null=False)
    discount_rate = models.IntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min_purchased_items = models.IntegerField(null=False)
    apply_to = models.CharField(max_length=8,
                                choices=(('Product', 'product'), ('Category', 'category')),
                                default="product",
                                null=False)
    target_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    target_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.discount_type,
                                                                   self.discount_rate,
                                                                   self.discount_amount,
                                                                   self.min_purchased_items,
                                                                   self.apply_to,
                                                                   self.target_product,
                                                                   self.target_category,
                                                                   self.name)

