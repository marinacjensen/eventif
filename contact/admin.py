from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'message', 'created_at', 'reply', 'replied_at']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone',
                    'message', 'created_at', 'reply', 'replied_at']
    list_filter = ['created_at', 'replied']

    actions = ['reply_check']

    def reply_check(self, request, queryset):
        count = queryset.update(replied=True)

        if count == 1:
            msg = "{} mensagem foi retornada."
        else:
            msg = "{} mensagens foram retornadas"

        self.message_user(request, msg.format(count))

    reply_check.short_description = 'Marcar como respondido'


admin.site.register(Contact, ContactModelAdmin)
