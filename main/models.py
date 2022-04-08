from django.db import models
from django.urls import reverse


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

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
    image = models.TextField(max_length=500)
    price = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='1')

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Одежду'
        verbose_name_plural = 'Одежды'

    def __str__(self):
        return self.name


class Sales(models.Model):
    category = models.ForeignKey(Category, related_name="sales", on_delete=models.CASCADE, default='1')
    gender = models.ForeignKey(Gender, related_name="sales", on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100, db_index=True)
    image = models.TextField(max_length=500)
    old_price = models.CharField(max_length=500)
    new_price = models.CharField(max_length=500)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name


class Gift(models.Model):
    gender = models.ForeignKey(Gender, related_name="gift", on_delete=models.CASCADE, default='1')
    image = models.TextField(max_length=500)
    price = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    include_description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'




