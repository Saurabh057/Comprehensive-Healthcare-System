# Generated by Django 2.2 on 2021-05-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0024_record_feedst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='feedst',
        ),
    ]
