# Generated by Django 4.1 on 2022-09-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0003_alter_asset_personal_device_alter_asset_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='warranty_expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]