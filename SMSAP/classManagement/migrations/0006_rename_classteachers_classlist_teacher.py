# Generated by Django 4.0.6 on 2022-07-23 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0005_alter_classlist_classteachers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classlist',
            old_name='classTeachers',
            new_name='Teacher',
        ),
    ]
