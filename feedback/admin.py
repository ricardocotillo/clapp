from django.contrib import admin
from .models import UserComment, ClubComment, MatchComment

admin.site.register(UserComment)
admin.site.register(ClubComment)
admin.site.register(MatchComment)
