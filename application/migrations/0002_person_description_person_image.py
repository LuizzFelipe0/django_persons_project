# Generated by Django 4.1.7 on 2023-03-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default='default_persons.jpg', upload_to='pictures'),
        ),
    ]
