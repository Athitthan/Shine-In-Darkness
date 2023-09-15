# Generated by Django 3.2.19 on 2023-08-31 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysocialapp', '0007_auto_20230830_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
    ]