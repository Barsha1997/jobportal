# Generated by Django 3.1.6 on 2021-04-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='aboutme',
            field=models.TextField(blank=True, null=True),
        ),
    ]
