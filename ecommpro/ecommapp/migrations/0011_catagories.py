# Generated by Django 5.0.2 on 2024-04-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0010_products_sale_alter_products_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=250)),
            ],
        ),
    ]
