from django.contrib import admin
from .models import userFormsDemo
from .models import userDemoForms
# Register your models here.

class serviceAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','boollean']
    
admin.site.register(userFormsDemo,serviceAdmin)


# demo purposes
class serviceDemoAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','phone','boollean']
    
admin.site.register(userDemoForms,serviceDemoAdmin)
