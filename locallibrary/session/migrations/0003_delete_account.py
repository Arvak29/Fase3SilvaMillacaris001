# Generated by Django 3.1.2 on 2020-11-27 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
