# Generated by Django 2.1 on 2018-08-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='Langage',
            new_name='Language',
        ),
    ]
