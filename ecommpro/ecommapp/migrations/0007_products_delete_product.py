# Generated by Django 5.0.2 on 2024-03-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0006_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('categories', models.CharField(choices=[('Electronic', 'electronic'), ('Fashion', 'Fashion'), ('Grocery', 'Grocery'), ('Home & Furniture', 'Home & furniture'), ('Mobiles', 'mobiles'), ('Appliances', 'Appliance')], max_length=250)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='ecommapp/static/image/uploads')),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
