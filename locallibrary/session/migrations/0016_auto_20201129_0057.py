# Generated by Django 3.1.2 on 2020-11-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0015_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.png', null=True, upload_to=''),
        ),
    ]
