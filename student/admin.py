from django.contrib import admin
from .models import Students, Address
from import_export.admin import ImportExportModelAdmin


@admin.register(Students)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'birth_date', 'address', 'status')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email', 'birth_date', 'address', 'status')
    ordering = ('first_name', 'username')
    search_fields = ('id', 'first_name', 'last_name', 'username', )
    autocomplete_fields = ("address",)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'country', 'city', 'street',)
    list_display_links = ('id', 'country', 'city', 'street')
    ordering = ('country', 'city', )
    search_fields = ('id', 'country', 'city', 'street')





