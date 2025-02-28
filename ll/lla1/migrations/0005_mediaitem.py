# Generated by Django 4.2.16 on 2024-09-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lla1', '0004_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
