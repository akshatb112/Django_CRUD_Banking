# Generated by Django 3.2 on 2021-04-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=100)),
                ('bcity', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'branch',
            },
        ),
    ]
