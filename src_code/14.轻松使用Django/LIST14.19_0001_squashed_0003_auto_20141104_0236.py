# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc

# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# polls.migrations.0003_auto_20141104_0236

class Migration(migrations.Migration):

    replaces = [(b'polls', '0001_initial'), (b'polls', '0002_poll_pub_date'), (b'polls', '0003_auto_20141104_0236')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                # 删除下面第一行，添加下面第二行
                # ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 11, 4, 1, 22, 22, 729029, tzinfo=utc), verbose_name=b'date published')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # 删除以下被注释的部分
        # migrations.RunPython(
        #     code=polls.migrations.0003_auto_20141104_0236.forward_pub_date_by_one_day,
        #     reverse_code=polls.migrations.0003_auto_20141104_0236.backward_pub_date_by_one_day,
        #     atomic=True,
        # ),
    ]
