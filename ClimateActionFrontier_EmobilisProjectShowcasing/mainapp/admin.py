from django.contrib import admin

from mainapp.models import Employee

# Register your models here.
admin.site.site_header = "ClimateActionFrontier"
admin.site.index_title = ("CAF server"
                          "")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', "dob", "disabled"]
    search_fields = ['name', 'email']
    list_filter = ["disabled"]


admin.site.register(Employee, EmployeeAdmin)


# # *****************************************************************
# # django_project/users/admin.py
# from django.contrib import admin
# from .models import SubscribedUsers
#
# class SubscribedUsersAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name', 'created_date')
#
#
# admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
# # **************************************************************************