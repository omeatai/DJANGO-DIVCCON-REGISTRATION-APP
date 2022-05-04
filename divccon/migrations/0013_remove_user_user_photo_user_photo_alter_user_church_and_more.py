# Generated by Django 4.0.4 on 2022-05-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divccon', '0012_delete_church_alter_user_diocese_alter_user_province_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='church',
            field=models.CharField(default='NONE', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='committee',
            field=models.CharField(default='NONE', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(default='DELEGATE', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='diocese',
            field=models.CharField(default='NONE', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='province',
            field=models.CharField(choices=[('', '---Select your Province---'), ('INSTITUTION', 'INSTITUTION'), ('ABA', 'ABA PROVINCE'), ('ABUJA', 'ABUJA PROVINCE'), ('BENDEL', 'BENDEL PROVINCE'), ('ENUGU', 'ENUGU PROVINCE'), ('IBADAN', 'IBADAN PROVINCE'), ('JOS', 'JOS PROVINCE'), ('KADUNA', 'KADUNA PROVINCE'), ('KWARA', 'KWARA PROVINCE'), ('LAGOS', 'LAGOS PROVINCE'), ('LOKOJA', 'LOKOJA PROVINCE'), ('NIGERDELTA', 'NIGER DELTA PROVINCE'), ('OFTHENIGER', 'OF THE NIGER PROVINCE'), ('ONDO', 'ONDO PROVINCE'), ('OWERRI', 'OWERRI PROVINCE'), ('CANA', 'CANA PROVINCE')], default='NONE', max_length=50),
        ),
    ]