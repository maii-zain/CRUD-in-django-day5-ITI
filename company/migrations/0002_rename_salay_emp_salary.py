# Generated by Django 5.0.2 on 2024-02-21 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='salay',
            new_name='salary',
        ),
    ]
