from django.contrib import admin
from .models import Site,tags, UserProfile

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    filter_horizontal =('tags', )

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'bio', 'phone_number', 'is_mvp']
    list_editable=[ 'bio', 'phone_number', 'is_mvp']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Site,SiteAdmin)
admin.site.register(tags)
