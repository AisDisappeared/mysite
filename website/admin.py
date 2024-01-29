from django.contrib import admin
from .models import contact,Newsletter


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('name', 'email','subject', 'created_date')
    list_filter = ('subject',)
    search_fields = ('name', 'subject' , 'email')
    # ordering = ('-created_date',)
    
    
admin.site.register(contact, ContactAdmin) 
admin.site.register(Newsletter)