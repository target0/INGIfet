#coding: utf-8

import datetime, web, pyqrcode
from models import Entry

def float2str(f):
    return "{:.2f}".format(f)

def get_object_or_404(model, **kwargs):
    try:
        obj = model.get(**kwargs)
        return obj
    except Entry.DoesNotExist:
        raise web.notfound()

def datetime2str(dt):
    dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f") #TODO assez moche, dépend du résultat de SQLite..
    return dt.strftime('%d/%m/%y %H:%M')

