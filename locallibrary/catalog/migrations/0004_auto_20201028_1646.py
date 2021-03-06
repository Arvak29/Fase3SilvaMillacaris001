# Generated by Django 3.1.2 on 2020-10-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201028_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinstance',
            name='stock',
            field=models.CharField(blank=True, choices=[('o', 'Out of stock'), ('a', 'Available'), ('p', 'Pre-order'), ('c', 'Coming soon')], default='a', help_text='Game availability', max_length=1),
        ),
    ]
