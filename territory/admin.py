from django.contrib import admin
from territory.models import Region, Constituency, PollingStation, District
# Register your models here.

admin.site.register(Region)
admin.site.register(District)
admin.site.register(PollingStation)
admin.site.register(Constituency)