# Generated by Django 3.2.3 on 2022-02-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmark', '0004_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
