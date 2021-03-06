# Generated by Django 3.1.4 on 2020-12-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=15)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=2084)),
            ],
        ),
    ]
