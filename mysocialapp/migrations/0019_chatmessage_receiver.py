# Generated by Django 3.2.19 on 2024-01-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysocialapp', '0018_chatmessage_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='receiver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
