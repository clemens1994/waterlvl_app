from urllib.request import urlopen
from django.db import models
import time
import datetime
import logging
import logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)


# Create your models here.

url = "https://www.hnd.bayern.de/pegel/isar/muenchen-himmelreichbruecke-16515005/tabelle?methode=wasserstand&"

page_with_waterlevel_list = urlopen(url)

html_bytes = page_with_waterlevel_list.read()

html = html_bytes.decode("utf-8")


def get_water_level():

    start_index = html.find("<td >")

    if not start_index > -1:
        return

    end_index = html.find("</td>")
    end_index = end_index + html[end_index+1:].find("</td>") + 1

    line = html[start_index+5:end_index]

    return line[41:]