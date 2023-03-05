# Generated by Django 4.1.7 on 2023-03-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('conposition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('categoty', models.CharField(choices=[('CR', 'Curd'), ('ML', 'milk'), ('LS', 'Lassi'), ('MS', 'milkshake'), ('PN', 'paneer'), ('GH', 'Ghee'), ('CZ', 'Cheeae'), ('IC', 'Ice-Cremas')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
