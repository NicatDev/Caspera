# Generated by Django 5.0 on 2023-12-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_blog_categoy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='categoy',
            new_name='category',
        ),
    ]
