from django.contrib import admin

from .models import Topic, Entry, Media

admin.site.register(Media)
admin.site.register(Topic)
admin.site.register(Entry)

