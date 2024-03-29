# Generated by Django 3.2.19 on 2024-01-24 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysocialapp', '0014_auto_20240119_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_users', to='mysocialapp.appuser')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='mysocialapp.appuser')),
            ],
            options={
                'unique_together': {('current_user', 'friend')},
            },
        ),
    ]
