from django.contrib import admin
from .models import Sport, Club, Membership, ClubImage

admin.site.register(Sport)
admin.site.register(Club)
admin.site.register(Membership)
admin.site.register(ClubImage)
