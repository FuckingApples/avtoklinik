from django.db import models

class Work(models.Model):

    # простые поля
    name = models.CharField(
        verbose_name="Название",
        blank=True, null=True
    )

    member = models.CharField(
        verbose_name="Исполнитель",
        blank=True, null=True
    )

    category = models.CharField(
        verbose_name="Категория",
        blank=True, null=True
    )

    price = models.DecimalField(
        verbose_name="Стоимость",
        blank=True, null=True
    )

    norm_time = models.DecimalField(
        verbose_name="Норма времени",
        blank=True, null=True
    )

    max_discount = models.DecimalField(
        verbose_name="Максимальная скидка (%)",
        blank=True, null=True
    )

    coefficient = models.DecimalField(
        verbose_name="Коэффициент",
        blank=True, null=True
    )

    multiplicity = models.PositiveIntegerField(
        verbose_name="Кратность",
        blank=True, null=True
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        blank=True, null=True
    )

    barcode = models.CharField(
        verbose_name="Штрихкод",
        blank=True, null=True
    )

    work_code = models.CharField(
        verbose_name="Код работы",
        blank=True, null=True
    )

    #   связанные поля

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="works",
    )

    hourly_wage = models.ForeignKey(
        'HourlyWage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="works",
        verbose_name="Нормочас"
    )

    related_works = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='related_to',
        verbose_name="Связанные работы"
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Номенкулатуры"
    )

    def __str__(self):
        return self.name
