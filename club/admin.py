from django.contrib import admin
from .models import Club, Membership


class ClubAdmin(admin.ModelAdmin):
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.base_fields.get('logo').required = False
        return form


admin.site.register(Club, ClubAdmin)
admin.site.register(Membership)
