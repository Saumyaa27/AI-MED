# Generated by Django 3.0.8 on 2020-11-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0031_auto_20201109_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=9, null=True),
        ),
    ]
