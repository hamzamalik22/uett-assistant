# Generated by Django 5.0.4 on 2024-04-27 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uettApp', '0002_department_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='department',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]