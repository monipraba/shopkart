# Generated by Django 5.0.1 on 2024-03-22 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_product_search_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='Products',
            new_name='description',
        ),
    ]
