# Generated by Django 4.1.5 on 2023-01-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BACKENDapp', '0006_contactusdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallerydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('IMAGE', models.ImageField(blank=True, null=True, upload_to='Gallery')),
            ],
        ),
    ]
