from django.contrib import admin
from testApp.models import (
    Contact,
    Group)
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "address",
        "created_date",
        "updated_date"
    ]

class GroupAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_date",
        "updated_date"
    ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Group, GroupAdmin)