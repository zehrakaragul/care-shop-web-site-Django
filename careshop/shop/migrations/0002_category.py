# Generated by Django 4.1.3 on 2023-04-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategorismi', models.CharField(max_length=70)),
                ('slug', models.CharField(max_length=70)),
            ],
        ),
    ]
