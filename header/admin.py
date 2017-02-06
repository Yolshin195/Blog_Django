from django.contrib import admin
from header.models import Header

# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    filds = ["header_title"]


admin.site.register(Header, HeaderAdmin)
