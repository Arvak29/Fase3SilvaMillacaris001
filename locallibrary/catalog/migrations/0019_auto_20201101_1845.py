# Generated by Django 3.1.2 on 2020-11-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_game_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
