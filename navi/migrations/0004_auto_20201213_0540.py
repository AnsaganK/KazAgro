# Generated by Django 3.1.4 on 2020-12-12 23:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0003_auto_20201213_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agrohym',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 13, 5, 40, 50, 745503), null=True),
        ),
        migrations.AlterField(
            model_name='agrohym',
            name='samples',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agrohym', to='navi.samples'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 13, 5, 40, 50, 744542), null=True),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='samples',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laboratory', to='navi.samples'),
        ),
        migrations.AlterField(
            model_name='preparation',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 13, 5, 40, 50, 735579), null=True),
        ),
        migrations.AlterField(
            model_name='preparation',
            name='samples',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preparation', to='navi.samples'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='nowTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 13, 5, 40, 50, 735579), null=True),
        ),
        migrations.AlterField(
            model_name='selection',
            name='samples',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selection', to='navi.samples'),
        ),
    ]
