from django.contrib import admin
from notes.models import Categories, Links, Notes

admin.site.register(Categories)
admin.site.register(Notes)
admin.site.register(Links)