"""Admin settings"""
from django.contrib import admin

from social_auth.models import UserSocialAuth, Nonce, Association


class UserSocialAuthOption(admin.ModelAdmin):
    """Social Auth user options"""
    list_display = ('id', 'user', 'provider', '_uid')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    list_filter = ('provider',)
    raw_id_fields = ('user',)
    list_select_related = True
    
    def _uid(self, usa):
        link = None
        if usa.provider == 'facebook':
            link = '<a href="http://facebook.com/profile.php?id=%s" ' \
                'target="_blank">%s</a>'
        elif usa.provider == 'twitter':
            link = '<a href="twitter.com/#!/%s" target="_blank">%s</a>'
            
        if link:
            link = link % (usa.uid, usa.uid)

        return link or usa.uid
    _uid.allow_tags = True


class NonceOption(admin.ModelAdmin):
    """Nonce options"""
    list_display = ('id', 'server_url', 'timestamp', 'salt')
    search_fields = ('server_url',)


class AssociationOption(admin.ModelAdmin):
    """Association options"""
    list_display = ('id', 'server_url', 'assoc_type')
    list_filter = ('assoc_type',)
    search_fields = ('server_url',)


admin.site.register(UserSocialAuth, UserSocialAuthOption)
admin.site.register(Nonce, NonceOption)
admin.site.register(Association, AssociationOption)
