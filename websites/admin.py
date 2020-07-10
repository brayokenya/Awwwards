from django.contrib import admin
from .models import Dev,Site,tags

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(Dev)
admin.site.register(Site,SiteAdmin)
admin.site.register(tags)
