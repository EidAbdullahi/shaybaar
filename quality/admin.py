from django.contrib import admin
from .models import Image, Location, category,jobs,Contact, Video,Application

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category', )

admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
admin.site.register(category)
admin.site.register(jobs)
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(Application)

