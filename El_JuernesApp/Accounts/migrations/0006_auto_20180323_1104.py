# Generated by Django 2.0.3 on 2018-03-23 11:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Accounts', '0005_auto_20180323_1102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Machine_designer',
            new_name='Layout_designer',
        ),
    ]