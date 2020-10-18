# Generated by Django 3.1.2 on 2020-10-18 11:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201014_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=tinymce.models.HTMLField(default=0, max_length=1500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
