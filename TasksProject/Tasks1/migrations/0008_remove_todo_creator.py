# Generated by Django 5.0.2 on 2024-02-23 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks1', '0007_remove_todo_todoid_todo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Creator',
        ),
    ]
