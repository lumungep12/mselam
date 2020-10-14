from django.contrib import admin
from contact.models import feeds, newsMail

class feedsAdmin(admin.ModelAdmin):
    pass

class newsMailAdmin(admin.ModelAdmin):
    pass

admin.site.register(feeds, feedsAdmin)
admin.site.register(newsMail, newsMailAdmin)
