# Generated by Django 4.1 on 2022-09-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='registration_date',
            field=models.DateField(null=True),
        ),
    ]
