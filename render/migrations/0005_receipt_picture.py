# Generated by Django 5.0.1 on 2024-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0004_alter_product_discount_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='picture',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
