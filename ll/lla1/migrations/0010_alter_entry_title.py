# Generated by Django 4.2.16 on 2024-10-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lla1', '0009_entry_priority_topic_priority_alter_entry_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
