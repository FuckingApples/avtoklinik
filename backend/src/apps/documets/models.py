from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.organizations.models import Organization

class Documents(models.Model):
    # связь с организацией
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    # Простые поля
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование"
                            )

    cheque_Name = models.CharField(
        max_length=255,
        verbose_name="Наименование в чеке"
                                   )

    article = models.CharField(
        max_length=255,
        verbose_name="Артикул",
        blank=True,
        null=True
                                  )

    barcode = models.CharField(
        max_length=255,
        verbose_name="Штрихкод",
        blank=True,
        null=True
                               )

    quantity = models.PositiveIntegerField(
        verbose_name="Количество для списания",
        default=1
    )

    unit = models.CharField(
        max_length=10,
        verbose_name="Единица измерения",
        default='gramm'
    )

    cost_price = models.DecimalField(
        verbose_name="Себестоимость (за единицу)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    selling_price = models.DecimalField(
        verbose_name="Цена продажи (за единицу)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    max_discount = models.PositiveIntegerField(
        verbose_name="Максимальная скидка (%)",
        validators=[MaxValueValidator(100)],
        default=0
    )

    critical_stock = models.PositiveIntegerField(
        verbose_name="Критический остаток",
        default=1
    )

    desired_stock = models.PositiveIntegerField(
        verbose_name="Желаемый остаток"
    )

    net_weight = models.DecimalField(
        verbose_name="Масса нетто",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.001)]
    )

    gross_weight = models.DecimalField(
        verbose_name="Масса брутто",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.001)]
    )

    Country = models.CharField(
        max_length=255,
        verbose_name="Страна производитель"
    )

    # связанные поля
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents",
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
        related_name="documents",
        verbose_name="Производитель"
    )

    def __str__(self):
        return self.name
