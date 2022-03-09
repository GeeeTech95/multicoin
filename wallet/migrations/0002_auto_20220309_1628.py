# Generated by Django 3.0.5 on 2022-03-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawalapplication',
            name='coin',
        ),
        migrations.RemoveField(
            model_name='withdrawalapplication',
            name='wallet_address',
        ),
        migrations.AddField(
            model_name='withdrawalapplication',
            name='balance_type',
            field=models.CharField(choices=[('Referral', 'Referral'), ('Main', 'Main')], default=True, max_length=10),
            preserve_default=False,
        ),
    ]
