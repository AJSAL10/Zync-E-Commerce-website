# Generated by Django 4.1.4 on 2023-01-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BACKENDapp', '0004_alter_productdb_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='IMAGE',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]