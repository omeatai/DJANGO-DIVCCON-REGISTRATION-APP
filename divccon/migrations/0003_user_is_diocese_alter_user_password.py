# Generated by Django 4.0.4 on 2022-04-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divccon', '0002_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_diocese',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
