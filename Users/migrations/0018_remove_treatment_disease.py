# Generated by Django 3.0.8 on 2020-09-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0017_auto_20200924_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='Disease',
        ),
    ]
