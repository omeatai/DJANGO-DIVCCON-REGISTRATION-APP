# Generated by Django 4.0.4 on 2022-05-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divccon', '0018_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
