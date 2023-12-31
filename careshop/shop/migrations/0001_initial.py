# Generated by Django 4.1.3 on 2023-04-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('urunismi', models.CharField(max_length=50)),
                ('aciklama', models.TextField()),
                ('resimUrl', models.URLField()),
                ('fiyat', models.IntegerField()),
                ('fiyatbirim', models.CharField(max_length=10)),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
