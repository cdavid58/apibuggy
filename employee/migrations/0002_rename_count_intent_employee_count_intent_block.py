# Generated by Django 3.2.8 on 2022-12-08 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='count_intent',
            new_name='count_intent_block',
        ),
    ]