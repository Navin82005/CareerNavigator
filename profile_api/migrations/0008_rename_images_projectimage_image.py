# Generated by Django 4.2.4 on 2023-08-24 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0007_projectimage_name_alter_projectimage_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimage',
            old_name='images',
            new_name='image',
        ),
    ]
