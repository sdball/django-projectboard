from bigboard.models import Item
from django.conf.urls.defaults import *

archive_info = {
    'queryset': Item.objects.all(),
    'date_field': 'due_date',
}

month_archive_info = {
    'queryset': Item.objects.all(),
    'date_field': 'due_date',
    'month_format': '%m',
    'allow_empty': True,
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', archive_info),
    (r'^(?P<year>\d{4})/$', 'archive_year', archive_info),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'archive_month',
        month_archive_info
    ),
)
