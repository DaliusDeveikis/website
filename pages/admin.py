from django.contrib import admin
from django.utils.html import format_html

from .models import Service, Intro


class ServiceAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.image.url))

    thumbnail.short_description = 'Image'

    list_display = ('id', 'thumbnail', 'title', 'price', 'created_date', 'is_active')
    list_display_links = ('id', 'thumbnail', 'title', 'price')
    search_fields = ('title', 'price')
    list_filter = ['created_date', ]
    list_editable = ['is_active', ]


class IntroAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.image.url))

    thumbnail.short_description = 'Img'
    list_display = ('id', 'thumbnail', 'name', 'surname', 'profession', 'is_active')
    list_display_links = ('id', 'thumbnail', 'name', 'surname', 'profession')
    list_editable = ['is_active', ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Intro, IntroAdmin)
