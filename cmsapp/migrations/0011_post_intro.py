# Generated by Django 4.0.6 on 2022-09-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0010_remove_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
