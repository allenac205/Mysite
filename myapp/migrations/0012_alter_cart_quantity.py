# Generated by Django 4.1.1 on 2022-12-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_oderhistory_quantity_alter_oderhistory_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart", name="quantity", field=models.IntegerField(default=1),
        ),
    ]
