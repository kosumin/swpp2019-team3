# Generated by Django 2.2.8 on 2019-12-12 18:31

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('papersfeed', '0012_review_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionuser',
            name='type',
            field=django_mysql.models.EnumField(choices=[('owner', 'owner'), ('member', 'member'), ('pending', 'pending')]),
        ),
    ]