from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.organizations.models import Organization

class Product(models.Model):
    # связь с организацией
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="products",
    )

    # Простые поля
    name = models.TextField(
        verbose_name="Наименование"
                            )

    cheque_Name = models.TextField(
        verbose_name="Наименование в чеке"
                                  )

    article = models.TextField(
        verbose_name="Артикул",
        blank=True,
        null=True
                              )

    barcode = models.TextField(
        verbose_name="Штрихкод",
        blank=True,
        null=True
                               )

    quantity = models.PositiveIntegerField(
        verbose_name="Количество для списания",
        default=1
    )

    cost_price = models.DecimalField(
        verbose_name="Себестоимость (за единицу)",
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    selling_price = models.DecimalField(
        verbose_name="Цена продажи (за единицу)",
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    max_discount = models.PositiveIntegerField(
        verbose_name="Максимальная скидка (%)",
        validators=[MaxValueValidator(100)],
        null=True,
        blank=True,
        default=0
    )

    critical_stock = models.PositiveIntegerField(
        verbose_name="Критический остаток",
        null=True,
        blank=True,
        default=1
    )

    desired_stock = models.PositiveIntegerField(
        verbose_name="Желаемый остаток",
        null=True,
        blank=True,
    )

    net_weight = models.DecimalField(
        verbose_name="Масса нетто",
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.001)]
    )

    gross_weight = models.DecimalField(
        verbose_name="Масса брутто",
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.001)]
    )

    country = models.TextField(
        verbose_name="Страна производитель",
        null = True,
        blank = True
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        blank = True,
        null = True
    )

    # связанные поля
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категория"
    )

    sales_unit = models.ForeignKey(
        'MeasurementUnit',
        on_delete=models.PROTECT,
        related_name="products_sales_unit",
        verbose_name="Единица измерения для продажи"
    )

    write_off_unit = models.ForeignKey(
        'MeasurementUnit',
        on_delete=models.PROTECT,
        related_name="products_write_off_unit",
        verbose_name="Единица измерения для списания"
    )

    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Производитель"
    )

    def __str__(self):
        return self.name
