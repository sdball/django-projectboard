from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()

@register.filter
def bigboard_date_class(value):
    today = datetime.date.today()
    if value < today:
        return 'overdue'
    if value == today:
        return 'today'
    else:
        days_out = (value - today).days
        if days_out < 7:
            return 'thisweek'
        else:
            return 'nextweek'
