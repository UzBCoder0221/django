# Generated by Django 4.2 on 2023-04-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=256)),
                ('number', models.BigIntegerField()),
                ('secret_answer', models.CharField(max_length=300, null=True)),
                ('sign_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]