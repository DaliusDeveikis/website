# Generated by Django 2.2.10 on 2020-12-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
