# Generated by Django 5.0.4 on 2024-05-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titlepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlepage',
            name='topic',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
