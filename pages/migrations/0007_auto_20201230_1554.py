# Generated by Django 2.2.10 on 2020-12-30 15:54

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201230_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
