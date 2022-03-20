from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Clothes(models.Model):
    category = models.ForeignKey(Category, related_name="clothes", on_delete=models.CASCADE, default='1')
    gender = models.ForeignKey(Gender, related_name="clothes", on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
