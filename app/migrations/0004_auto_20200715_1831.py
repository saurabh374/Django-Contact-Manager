# Generated by Django 3.0.6 on 2020-07-15 13:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200715_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 18, 31, 9, 536917)),
        ),
    ]