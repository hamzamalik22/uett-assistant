# Generated by Django 5.0.4 on 2024-04-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uettApp', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='credit_hour',
            field=models.IntegerField(default=3),
        ),
    ]
