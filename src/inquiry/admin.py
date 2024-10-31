from django.contrib import admin
from .models import ClientInfo, MessageInfo


# TODO: More detail

class MessageInfoAdmin(admin.ModelAdmin):
    fields = ('msg_subject', 'msg_text', 'msg_client', 'is_deal')
    list_display = ('msg_subject', 'msg_text', 'msg_client', 'created_at', 'is_deal', 'dealt_at')
    list_display_links = ('msg_subject', 'msg_client')
    ordering = ('is_deal', '-created_at',)

class MessageInfoInline(admin.TabularInline):
    model = MessageInfo
    extra = 0
    show_change_link = True


class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('cli_company', 'cli_phone', 'cli_email', 'created_at', 'updated_at', 'was_connected_recently')


admin.site.register(ClientInfo, ClientInfoAdmin)
admin.site.register(MessageInfo, MessageInfoAdmin)
