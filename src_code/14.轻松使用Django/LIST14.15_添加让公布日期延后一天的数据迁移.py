# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations


def forward_pub_date_by_one_day(apps, schema_editor):
    Poll = apps.get_model('polls', 'Poll')
    for poll in Poll.objects.all():
        poll.pub_date += datetime.timedelta(days=1)
        poll.save()


def backward_pub_date_by_one_day(apps, schema_editor):
    Poll = apps.get_model('polls', 'Poll')
    for poll in Poll.objects.all():
        poll.pub_date -= datetime.timedelta(days=1)
        poll.save()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_pub_date'),
    ]

    operations = [
        migrations.RunPython(forward_pub_date_by_one_day,
                             backward_pub_date_by_one_day)
    ]
