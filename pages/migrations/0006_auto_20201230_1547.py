# Generated by Django 2.2.10 on 2020-12-30 15:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201230_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[500, 300], upload_to='photos/%Y/%m/%d/'),
        ),
    ]