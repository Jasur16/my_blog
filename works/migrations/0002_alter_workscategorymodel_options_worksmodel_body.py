# Generated by Django 4.0.5 on 2022-06-29 15:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workscategorymodel',
            options={'verbose_name': 'work category', 'verbose_name_plural': 'works categories'},
        ),
        migrations.AddField(
            model_name='worksmodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None),
            preserve_default=False,
        ),
    ]
