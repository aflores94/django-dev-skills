# Generated by Django 2.2 on 2019-06-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill',
            field=models.CharField(default='Python', max_length=100),
            preserve_default=False,
        ),
    ]
