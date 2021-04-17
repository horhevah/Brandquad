from django.contrib import admin
from .models import ApacheLog


# admin.site.register(ApacheLog)
# Register your models here.

class ApacheLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'data_time', 'method', 'status_code')
    list_display_links = ('ip_address', 'data_time', 'method', 'status_code')
    search_fields = ('ip_address','data_time','method','status_code')


admin.site.register(ApacheLog, ApacheLogAdmin)

# log = ApacheLog(ip_address=ip_address, data_time=date, method=method, url=url, status_code=status_code, size=size)
