# Generated by Django 5.0 on 2024-03-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='ecommapp/static/image/upload'),
        ),
    ]
