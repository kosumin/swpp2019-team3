# Generated by Django 2.2.5 on 2019-12-04 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papersfeed', '0009_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('-modification_date',)},
        ),
    ]
