# Generated by Django 4.0.3 on 2022-04-01 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('image', models.TextField(max_length=500)),
                ('old_price', models.CharField(max_length=500)),
                ('new_price', models.CharField(max_length=500)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='main.category')),
                ('gender', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='main.gender')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('available', models.BooleanField(default=True)),
                ('include_description', models.TextField(max_length=500)),
                ('gender', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='gift', to='main.gender')),
            ],
            options={
                'verbose_name': 'Gift_box',
                'verbose_name_plural': 'Gift_boxes',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('image', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='1', max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.category')),
                ('gender', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.gender')),
            ],
            options={
                'verbose_name': 'Cloth',
                'verbose_name_plural': 'Clothes',
                'ordering': ('name',),
            },
        ),
    ]