# Generated by Django 3.2.4 on 2021-06-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_q', '0014_schedule_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
