# Generated by Django 2.2.8 on 2019-12-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papersfeed', '0013_collectionuser_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photoIndex',
            field=models.IntegerField(default=0),
        ),
    ]
