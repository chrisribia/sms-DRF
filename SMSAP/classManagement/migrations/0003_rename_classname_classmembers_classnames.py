# Generated by Django 4.0.6 on 2022-07-23 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0002_rename_classname_classlist_classnames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classmembers',
            old_name='className',
            new_name='classNames',
        ),
    ]