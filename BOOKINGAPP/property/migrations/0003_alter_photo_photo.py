# Generated by Django 3.2.16 on 2023-01-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]