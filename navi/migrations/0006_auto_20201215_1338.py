# Generated by Django 3.1.4 on 2020-12-15 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0005_auto_20201214_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Активность', 'verbose_name_plural': 'Активности'},
        ),
        migrations.AlterField(
            model_name='agrohym',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 13, 38, 13, 669813), null=True),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 13, 38, 13, 669813), null=True),
        ),
        migrations.AlterField(
            model_name='preparation',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 13, 38, 13, 669813), null=True),
        ),
        migrations.AlterField(
            model_name='selection',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 13, 38, 13, 669813), null=True),
        ),
    ]