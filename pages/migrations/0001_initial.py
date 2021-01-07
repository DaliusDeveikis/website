# Generated by Django 2.2.10 on 2020-12-30 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantagesOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_title', models.CharField(max_length=100)),
                ('option_slug', models.CharField(help_text='A system friendly version of the value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdvantagesOptionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(max_length=100)),
                ('advantage', models.ManyToManyField(related_name='advantage_choise', to='pages.AdvantagesOption')),
            ],
        ),
        migrations.AddField(
            model_name='advantagesoption',
            name='option_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='pages.AdvantagesOptionSet'),
        ),
    ]
