# Generated by Django 2.2.12 on 2020-10-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailauth',
            name='email_e',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]