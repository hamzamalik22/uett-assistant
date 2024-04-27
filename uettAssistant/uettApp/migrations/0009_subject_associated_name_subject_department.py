# Generated by Django 5.0.4 on 2024-04-27 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uettApp', '0008_alter_semester_associated_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='associated_name',
            field=models.CharField(default='not_assigned', max_length=200),
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='uettApp.department'),
        ),
    ]
