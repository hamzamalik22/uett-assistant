# Generated by Django 5.0.4 on 2024-05-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titlepage', '0002_titlepage_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlepage',
            name='dep',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='titlepage',
            name='section',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
