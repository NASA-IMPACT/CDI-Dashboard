# Generated by Django 3.1.13 on 2021-10-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20211024_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterlist',
            name='cdi_themes',
            field=models.CharField(max_length=500, null=True),
        ),
    ]