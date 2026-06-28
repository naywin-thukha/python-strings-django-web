from django.contrib import admin

from strings_app.models import StringExample


@admin.register(StringExample)
class StringExampleAdmin(admin.ModelAdmin):
    list_display = ("text", "category", "created_at")
    search_fields = ("text", "notes")
