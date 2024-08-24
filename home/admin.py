from django.contrib import admin
from .models import Project, Tag
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    model = Project

    list_display = (
        "id",
        "title",
        "slug",
        
       
    )
    list_filter = (
       
        "date_created",
    )
    list_editable = (
        "title",
        
        "slug",
       
    )
    search_fields = (
        "title",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            
        )
    }
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
