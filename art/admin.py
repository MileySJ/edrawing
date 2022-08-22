from django.contrib import admin
from .models import Artist, Art
from django.conf import settings


class ArtistDisplay(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'last_login',)

    @admin.display(empty_value='unknown')
    def username(self, obj):
        return obj.account.username
    
    @admin.display(empty_value='unknown')
    def date_joined(self, obj):
        return obj.account.date_joined

    @admin.display(empty_value='unknown')
    def last_login(self, obj):
        return obj.account.last_login





admin.site.register(Artist, ArtistDisplay)
admin.site.register(Art)
