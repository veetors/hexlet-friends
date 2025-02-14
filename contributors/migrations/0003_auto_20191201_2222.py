# Generated by Django 2.2.6 on 2019-12-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_auto_20191128_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='is_tracked',
            field=models.BooleanField(default=True, verbose_name='tracked'),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_tracked',
            field=models.BooleanField(default=True, verbose_name='tracked'),
        ),
        migrations.AddField(
            model_name='repository',
            name='is_tracked',
            field=models.BooleanField(default=True, verbose_name='tracked'),
        ),
    ]
