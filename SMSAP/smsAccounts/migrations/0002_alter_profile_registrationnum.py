# Generated by Django 4.0.6 on 2022-07-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsAccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='RegistrationNum',
            field=models.CharField(default=0.9597299608795901, max_length=255, unique=True),
        ),
    ]