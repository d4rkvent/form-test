
from django.contrib import admin
from .models import Page


class PostAdmin(admin.ModelAdmin):
    list_display = ["title"]


    search_fields = ["title"]
    class Meta:
        model = Page


admin.site.register(Page, PostAdmin)