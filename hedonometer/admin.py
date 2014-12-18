from django.contrib import admin

# Register your models here.
# No models for now
# Eventually we can create a database for the big events
from hedonometer.models import Event,Book,Happs,Embeddable

from django.contrib.auth import get_user_model
User = get_user_model()

class EventAdmin(admin.ModelAdmin):
    search_fields = ('longer',)
    ordering = ('-date',)
    save_as = True
    list_display = ('date','caption','importance','x','y','shorter',)
    list_display_links = ('caption',)
    list_editable = ('importance','x','y',)

class HappsAdmin(admin.ModelAdmin):
    list_display = ('date','value',)

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title','author',)
    list_display = ('title','author','language',)
    list_display_links = ('title',)
    list_editable = ('language',)

admin.site.register(Event,EventAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Happs,HappsAdmin)
admin.site.register(Embeddable)
