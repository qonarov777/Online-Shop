# Generated by Django 4.1.3 on 2022-11-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_shopproduct_alter_arrived_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Shop detail/')),
            ],
            options={
                'verbose_name': 'Shop Detail',
                'verbose_name_plural': 'Shop Details',
            },
        ),
    ]
