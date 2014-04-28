from django.contrib import admin

from .models import NeighborhoodCouncil


class NeighborhoodCouncilAdmin(admin.ModelAdmin):
    list_display = ('label', 'cname1', 'cemail1', 'ctitle1',)


admin.site.register(NeighborhoodCouncil, NeighborhoodCouncilAdmin)
