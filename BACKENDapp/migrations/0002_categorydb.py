# Generated by Django 4.1.4 on 2023-01-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BACKENDapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('DISCRIPTION', models.CharField(blank=True, max_length=50, null=True)),
                ('IMAGE', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
    ]
