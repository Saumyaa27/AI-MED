# Generated by Django 3.0.8 on 2020-09-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20200924_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='Disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Patients', to='Users.Disease'),
        ),
    ]
