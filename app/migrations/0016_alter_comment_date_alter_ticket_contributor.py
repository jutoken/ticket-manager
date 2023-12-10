# Generated by Django 5.0 on 2023-12-10 16:08

import app.models
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_comment_date_alter_ticket_contributor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 17, 8, 35, 418810), validators=[app.models.Comment.no_future]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='contributor',
            field=models.ForeignKey(limit_choices_to={'groups__name__in': ['Developpers', 'Clients']}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
