# Generated by Django 3.1.4 on 2020-12-22 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0015_auto_20201222_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcorm',
            old_name='countSamples',
            new_name='count',
        ),
    ]
