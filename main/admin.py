from django.contrib import admin
from .models import Crud

class CrudAdmin(admin.ModelAdmin):
    list_display = ["name","admit", "case", "refer", "scheme", "status"]
admin.site.register(Crud,CrudAdmin)


# Register your models here.
