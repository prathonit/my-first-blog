# Generated by Django 2.2.10 on 2020-02-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
