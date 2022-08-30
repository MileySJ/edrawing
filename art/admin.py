from django.contrib import admin
from .models import Artist, Art
from django.conf import settings
from django import forms





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

class ArtForm(forms.ModelForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        
        if not self.current_user.is_superuser:
            qs = self.fields['artist'].queryset
            qs = qs.filter(account=self.current_user)
            self.fields['artist'].queryset = qs

    class Meta:
        model = Art
        exclude = ('',)

class ArtAdmin(admin.ModelAdmin):
    form = ArtForm
    list_display = ('title', 'artist')

# a memorizar
    def get_form(self, request, *args, **kwargs):
        f = super().get_form(request, *args, **kwargs)
        f.current_user = request.user
        return f

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
