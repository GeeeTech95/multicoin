# Generated by Django 3.0.5 on 2022-05-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_settings_approve_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='approve_investment',
            field=models.BooleanField(default=False, verbose_name='Stop automatic investments'),
        ),
    ]
