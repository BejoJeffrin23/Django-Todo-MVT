# Generated by Django 3.0.1 on 2019-12-22 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20191222_1034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Todo',
        ),
    ]