from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name','phone','subject')






