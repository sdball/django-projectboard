from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from bigboard.models import Item, ItemForm
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)

def list(request):
    items = Item.objects.filter(due_date__gt=yesterday)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ItemForm()
    return render_to_response('bigboard/item_list.html',
                              {'object_list': items,
                               'form': form,
                               'MEDIA_URL': settings.MEDIA_URL})

def group_list(request, group):
    items = Item.objects.filter(groups__name=group).filter(
                                                    due_date__gt=yesterday)
    return render_to_response('bigboard/group_list.html',
                              {'object_list': items,
                               'group': group,
                               'MEDIA_URL': settings.MEDIA_URL})

def contact_list(request, contact):
   items = Item.objects.filter(contacts__name=contact).filter(
                                                   due_date__gt=yesterday)
   return render_to_response('bigboard/group_list.html',
                             {'object_list': items,
                              'group': contact,
                              'MEDIA_URL': settings.MEDIA_URL})
