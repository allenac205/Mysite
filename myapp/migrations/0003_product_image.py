# Generated by Django 4.1.1 on 2022-10-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
    ]