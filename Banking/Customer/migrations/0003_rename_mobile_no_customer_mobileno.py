# Generated by Django 3.2 on 2021-04-30 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20210430_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mobile_no',
            new_name='mobileno',
        ),
    ]