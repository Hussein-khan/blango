from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blango_auth.models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(User, UserAdmin)