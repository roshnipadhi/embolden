# Generated by Django 2.1 on 2018-09-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_text',
        ),
        migrations.AddField(
            model_name='card',
            name='text',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
