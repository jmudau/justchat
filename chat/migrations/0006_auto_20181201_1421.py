# Generated by Django 2.1.3 on 2018-12-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20181117_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='chats', to='chat.Contact'),
        ),
    ]
