# Generated by Django 3.1.13 on 2021-10-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20211024_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qaupdates',
            name='catalog_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
