# Generated by Django 5.1.3 on 2024-12-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.gif', upload_to='prf_pics'),
        ),
    ]
