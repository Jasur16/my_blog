from django.contrib import admin
from .models import WorksCategoryModel, WorksModel

@admin.register(WorksCategoryModel)
class WorksCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_link = ['id', 'name']
    search_fields = ['name']


@admin.register(WorksModel)
class WorksModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title', 'created_at']
    search_fields = ['title']