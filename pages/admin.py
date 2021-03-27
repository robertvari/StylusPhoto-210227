from django.contrib import admin

from .models import Contact, HomePage, AboutPageModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "facebook", "instagram"]
    search_fields = ["email", "phone"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(HomePage)
admin.site.register(AboutPageModel)
