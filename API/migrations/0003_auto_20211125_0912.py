# Generated by Django 3.2.9 on 2021-11-25 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20211125_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
