# Generated by Django 5.0.1 on 2024-02-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_profile_city_alter_profile_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]