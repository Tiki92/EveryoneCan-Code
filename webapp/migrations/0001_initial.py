# Generated by Django 2.1 on 2018-08-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('Date', models.DateTimeField(verbose_name='published date')),
                ('Langage', models.CharField(max_length=100)),
            ],
        ),
    ]
