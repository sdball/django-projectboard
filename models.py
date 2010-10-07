from django.db import models
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

class Group(models.Model):
    name = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=False, editable=False)
    groups = models.ManyToManyField(Group,
                                    verbose_name=("Groups associated with"
                                                  " this project"))
    contacts = models.ManyToManyField(Contact,
                                      verbose_name=("People associated with"
                                                    " this project"))
    
    class Meta:
        ordering = ['due_date']
    
    def __unicode__(self):
        return self.name

class ItemForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=SelectDateWidget(attrs={'class':'date'}),
        initial=datetime.date.today())
    due_time = forms.TimeField(widget=forms.TimeInput(), required=False)
    class Meta:
        model = Item

