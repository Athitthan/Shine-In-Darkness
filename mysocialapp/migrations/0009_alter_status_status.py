# Generated by Django 3.2.19 on 2023-09-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysocialapp', '0008_auto_20230831_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
