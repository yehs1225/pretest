# Generated by Django 3.0.9 on 2022-04-06 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='order_number',
            new_name='product_number',
        ),
    ]
