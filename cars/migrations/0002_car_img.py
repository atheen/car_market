# Generated by Django 2.2.13 on 2020-09-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
