# Generated by Django 4.1.7 on 2023-04-19 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_categories_contents_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='categoies',
            new_name='title',
        ),
    ]