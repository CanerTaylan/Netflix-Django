# Generated by Django 4.1.7 on 2023-04-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_alter_profil_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='password',
            field=models.CharField(max_length=50, null=True, verbose_name='Şifre'),
        ),
        migrations.AddField(
            model_name='profil',
            name='password_active',
            field=models.BooleanField(default=False, verbose_name='Şifrele'),
        ),
    ]
