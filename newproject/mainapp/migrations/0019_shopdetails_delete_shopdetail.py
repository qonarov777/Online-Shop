# Generated by Django 4.1.3 on 2022-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_shopdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Shop detail/')),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Shop Detail',
                'verbose_name_plural': 'Shop Details',
            },
        ),
        migrations.DeleteModel(
            name='Shopdetail',
        ),
    ]
