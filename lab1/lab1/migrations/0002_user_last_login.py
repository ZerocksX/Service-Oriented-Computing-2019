# Generated by Django 2.2.6 on 2019-11-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]