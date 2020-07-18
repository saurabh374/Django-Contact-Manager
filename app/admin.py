from django.contrib import admin
from app.models import Contact
from django.contrib.auth.models import Group
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'info', 'phone')
    list_editable = ('info',)
    list_per_page = 10
    search_field = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
