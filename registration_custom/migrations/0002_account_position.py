# Generated by Django 4.1 on 2022-10-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='position',
            field=models.CharField(max_length=1000, null=True, verbose_name='Должность'),
        ),
    ]
