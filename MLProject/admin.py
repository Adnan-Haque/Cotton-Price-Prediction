from django.contrib import admin

# Register your models here.
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from MLProject.models import User,User_manager

# # Define an inline admin descriptor for MyUser model
# # which acts a bit like a singleton
# class MyUserInline(admin.StackedInline):
#     model = User
#     can_delete = False
#     verbose_name_plural = 'User'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (MyUserInline,)

# class MyUser_managerInline(admin.StackedInline):
#     model = User_manager
#     can_delete = False
#     verbose_name_plural = 'User_manager'

# # Define a new User admin
# class User_managerAdmin(BaseUserAdmin):
#     inlines = (MyUser_managerInline,)

# # Re-register UserAdmin
# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# # admin.site.unregister(User_manager)
# admin.site.register(User_manager, User_managerAdmin)

from .models import User

admin.site.register(User)