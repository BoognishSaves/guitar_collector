# Generated by Django 4.1.1 on 2022-10-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_artist_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='band',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
