# Generated by Django 5.0.2 on 2024-02-23 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks1', '0008_remove_todo_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Tasks1.user'),
            preserve_default=False,
        ),
    ]