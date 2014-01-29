from django.contrib import admin

from external_data_sync.admin import DataSourceAdmin

from .models import LaDataSource


class LaDataSourceAdmin(DataSourceAdmin):
    pass

admin.site.register(LaDataSource, LaDataSourceAdmin)
