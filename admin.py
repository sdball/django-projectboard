from django.contrib import admin
from bigboard.models import Group, Contact, Item

class GroupAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'due_date')
    list_filter = ('due_date', 'groups', 'contacts')
    date_hierarchy = 'due_date'
    filter_horizontal = ('contacts', 'groups',)
    fieldsets = (
        ('Upcoming Project', {
            'fields': ('name', 'description')
        }),
        ('Schedule', {
            'fields': ('due_date', 'due_time')
        }),
        (None, {
            'fields': ('groups', 'contacts')
        }),
    )

admin.site.register(Group, GroupAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Item, ItemAdmin)
