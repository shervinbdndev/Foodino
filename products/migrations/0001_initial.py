# Generated by Django 5.0 on 2023-12-20 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90, null=True, verbose_name='نام غذا')),
                ('price', models.CharField(blank=True, max_length=15, null=True, verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/foods', verbose_name='عکس')),
                ('quantity', models.IntegerField(blank=True, default=10, null=True, verbose_name='تعداد')),
                ('ingredients', models.TextField(blank=True, max_length=150, null=True, verbose_name='مواد اولیه')),
                ('food_type', models.CharField(blank=True, choices=[('fast-food', 'فست فود'), ('drink', 'نوشیدنی'), ('salad', 'سالاد')], max_length=50, null=True, verbose_name='نوع غذا')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذاها',
            },
        ),
    ]
