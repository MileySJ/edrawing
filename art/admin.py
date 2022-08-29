from django.contrib import admin
from .models import Artist, Art
from django.conf import settings


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'last_login', 'art_count')

    @admin.display(empty_value='unknown')
    def username(self, obj):
        return obj.account.username
    
    @admin.display(empty_value='unknown')
    def date_joined(self, obj):
        return obj.account.date_joined

    @admin.display(empty_value='unknown')
    def last_login(self, obj):
        return obj.account.last_login

    @admin.display(empty_value='0')
    def art_count(self, obj):
        return obj.arts.count()


class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(artist__in=request.user.artists.all())
        
    @admin.display(empty_value='unknown')
    def title(self, obj):
        return obj.title

    @admin.display(empty_value='unknown')
    def artist(self, obj):
        return obj.artist

    





admin.site.register(Artist, ArtistAdmin)
admin.site.register(Art, ArtAdmin)
