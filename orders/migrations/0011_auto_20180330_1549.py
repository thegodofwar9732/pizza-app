# Generated by Django 2.0.3 on 2018-03-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='details',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
