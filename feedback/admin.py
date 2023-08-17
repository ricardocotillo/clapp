from django.contrib import admin
from .models import Comment, Rating, Image


class ImageAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields.get('description').required = False
        return form


admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Image, ImageAdmin)
