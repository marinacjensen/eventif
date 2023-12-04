from django.contrib import admin
from django.utils.html import format_html
from core.models import Speaker, ContactSpeaker, Talk


class ContactInline(admin.TabularInline):
    model = ContactSpeaker
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}">', obj.photo)

    photo_img.short_description = 'foto'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)