# Generated by Django 4.2.16 on 2024-09-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lla1', '0007_rename_mediaitem_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='change it', max_length=50),
        ),
    ]
