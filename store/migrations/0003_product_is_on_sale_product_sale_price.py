# Generated by Django 5.0 on 2024-01-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_alter_product_p_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]