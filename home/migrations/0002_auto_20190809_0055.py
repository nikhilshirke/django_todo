# Generated by Django 2.2.4 on 2019-08-08 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='objective',
            new_name='task',
        ),
    ]