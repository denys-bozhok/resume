# Generated by Django 4.2.3 on 2023-08-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(upload_to='../images'),
        ),
    ]
