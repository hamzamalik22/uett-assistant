# Generated by Django 5.0.4 on 2024-04-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uettApp', '0005_subject_credit_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='associated_name',
            field=models.CharField(default='not_assigned', max_length=200),
        ),
    ]
