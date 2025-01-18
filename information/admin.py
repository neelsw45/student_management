from django.contrib import admin
from .models import Addmission,Contact

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    list_display=['id','sname','semail','sphoneno','senrollno','sadddate']

admin.site.register(Addmission,InformationAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phno','desc']

admin.site.register(Contact,ContactAdmin)

