# Generated by Django 2.2.16 on 2020-09-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ดร.วิชิต สมบัติ', max_length=300)),
                ('room', models.CharField(default='SC204', max_length=20)),
                ('extension', models.CharField(default='4446', max_length=20)),
            ],
        ),
    ]
