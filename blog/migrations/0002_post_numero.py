# Generated by Django 4.0.3 on 2022-05-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='numero',
            field=models.IntegerField(null=True),
        ),
    ]