# Generated by Django 4.0.6 on 2022-09-21 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petclassiffier', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlmodels',
            old_name='weihts',
            new_name='weights',
        ),
    ]
