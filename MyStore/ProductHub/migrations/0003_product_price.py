# Generated by Django 5.2.3 on 2025-06-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductHub', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
