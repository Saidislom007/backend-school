from django.contrib import admin
from .models import *

class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'views', 'likes')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
    list_editable = ('category',)
    readonly_fields = ('views', 'likes', 'created_at', 'updated_at')

admin.site.register(BlogPost)
admin.site.register(Teacher)
admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
admin.site.register(Achievement)
admin.site.register(LibraryItem)