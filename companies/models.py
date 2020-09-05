from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Contact(models.Model):
    """Phones or emails"""

    contact = models.CharField(verbose_name="Phone or email", max_length=150)
    is_phone = models.BooleanField(
        verbose_name="True - phone; False - email", default=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    generic_foreign_key = GenericForeignKey("content_type", "object_id")

    class Meta:
        db_table = "contacts"

    def __str__(self):
        return self.contact


class Company(models.Model):
    """The entity of company that offers stocks"""

    name = models.CharField(verbose_name="Name of company", max_length=256)
    avatar = models.ImageField(
        verbose_name="Avatar of company", upload_to="avatars/%Y/%m/%d"
    )
    contacts = GenericRelation(Contact)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return self.name


class Place(models.Model):
    """Company franchise"""

    address = models.TextField(verbose_name="Address")
    open_work_time = models.TimeField(
        verbose_name="Company open work time", blank=True, null=True
    )
    close_work_time = models.TimeField(
        verbose_name="Company close work time", blank=True, null=True
    )
    whole_day = models.BooleanField(verbose_name="24h per day", default=False)
    company = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, related_name="places"
    )
    contacts = GenericRelation(Contact)

    class Meta:
        db_table = "places"

    def __str__(self):
        return self.address


class Stock(models.Model):
    """The entity of stock offered by company"""

    name = models.CharField(verbose_name="Name of stock", max_length=256)
    image = models.ImageField(
        verbose_name="Image of stock", upload_to="stocks_images/%Y/%m/%d"
    )
    description = models.TextField(verbose_name="Description of stock")
    is_free = models.BooleanField(default=False)
    date_end = models.DateTimeField(
        verbose_name="Date end of stock", default=timezone.now
    )
    is_active = models.BooleanField(verbose_name="Active", default=True)
    places = models.ManyToManyField(to=Place, related_name="stocks", blank=True)

    class Meta:
        db_table = "stocks"

    def __str__(self):
        return self.name
