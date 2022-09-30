from django.db import models


class Order(models.Model):
    """Создание моделей."""
    number = models.PositiveSmallIntegerField()
    order_number = models.PositiveIntegerField()
    price_in_dollars = models.PositiveIntegerField()
    price_in_rubs = models.PositiveIntegerField(null=True, blank=True)
    supply_date = models.CharField(max_length=100)

    class Meta:
        """Сортировка по id."""

        ordering = ('number',)

    def __str__(self):
        """Метод __str__ возвращает номер заказа."""
        return str(self.order_number)
