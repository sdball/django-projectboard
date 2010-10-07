from bigboard.models import Item
from django.conf.urls.defaults import *
from django.views.generic.create_update import update_object, delete_object

urlpatterns = patterns('',
    (r'^(?P<object_id>\d+)/edit/$',
        update_object,
        {'model': Item, 'post_save_redirect': '/'}),
    (r'^(?P<object_id>\d+)/delete/$', delete_object,
        {'model': Item, 'post_delete_redirect': '/'}),
    (r'^group/(?P<group>[*\w]+)/$', 'bigboard.views.group_list'),
    (r'^contact/(?P<contact>.+)/$', 'bigboard.views.contact_list'),
    (r'^$', 'bigboard.views.list'),
)

item_info_dict = {
    'queryset': Item.objects.all(),
    'date_field': 'due_date',
}
