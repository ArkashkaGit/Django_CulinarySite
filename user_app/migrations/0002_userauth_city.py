# Generated by Django 4.2.7 on 2023-11-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauth',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]