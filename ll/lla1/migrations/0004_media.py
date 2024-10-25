# Generated by Django 4.2.16 on 2024-09-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lla1', '0003_alter_entry_options_topic_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
    ]
