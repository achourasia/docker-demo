import datetime
import os

from django.conf import settings


def record_container_stats(container_name):
    if (os.path.exists(settings.STATS_DIR)):
        with open('%s/%s.txt' % (settings.STATS_DIR, datetime.date.today()), 'a+') as f:
            f.write('%s\n' % container_name)
