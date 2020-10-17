from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Employer)
admin.site.register(Freelancer)


class employerInline(admin.StackedInline):
    model = Employer
    can_delete = False
    verbose_name_plural = 'epmployer'


# Define a new User admin



class freelancerrInline(admin.StackedInline):
    model = Freelancer
    can_delete = False
    verbose_name_plural = 'freelancer'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (employerInline,freelancerrInline)


admin.site.register(Category)
admin.site.register(Related_subject)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Project)


# Register your models here.
