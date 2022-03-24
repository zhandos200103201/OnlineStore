from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

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

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cloth'
        verbose_name_plural = 'Clothes'

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
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return self.name


class Gift(models.Model):
    gender = models.ForeignKey(Gender, related_name="gift", on_delete=models.CASCADE, default='1')
    image = models.TextField(max_length=500)
    price = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    include_description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Gift_box'
        verbose_name_plural = 'Gift_boxes'




