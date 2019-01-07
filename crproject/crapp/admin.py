from django.contrib import admin

# Register your models here.
from .models import Kitchen,Bedroom,Hall,Handles,Doors


admin.site.register(Bedroom)
admin.site.register(Kitchen)
admin.site.register(Hall)
admin.site.register(Handles)
admin.site.register(Doors)
