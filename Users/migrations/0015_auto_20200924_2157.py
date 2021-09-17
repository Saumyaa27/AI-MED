# Generated by Django 3.0.8 on 2020-09-24 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_auto_20200924_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='treatment',
            name='Disease',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Diseases', to='Users.Specialization')),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Specialization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='Doctors', to='Users.Specialization'),
            preserve_default=False,
        ),
    ]
