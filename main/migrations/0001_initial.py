# Generated by Django 5.1.7 on 2025-06-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scheme', models.CharField(max_length=100)),
                ('admit', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('case', models.CharField(max_length=100)),
                ('refer', models.CharField(max_length=100)),
            ],
        ),
    ]
