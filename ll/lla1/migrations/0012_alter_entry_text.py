# Generated by Django 4.2.16 on 2024-10-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lla1', '0011_alter_entry_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
