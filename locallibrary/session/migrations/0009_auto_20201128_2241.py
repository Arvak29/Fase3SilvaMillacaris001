# Generated by Django 3.1.2 on 2020-11-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20201128_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.png', upload_to=''),
        ),
    ]
