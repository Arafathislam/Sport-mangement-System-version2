from django.contrib import admin

# Register your models here.
from .models import Registration,Login

admin.site.register(Registration)
admin.site.register(Login)
