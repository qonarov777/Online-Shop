# Generated by Django 4.1.3 on 2022-11-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_products_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('title', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('cost_delate', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product arrived',
                'verbose_name_plural': 'Products arrived',
            },
        ),
    ]