from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

# Add Topic
admin.site.register(Topic)

# Add Room
admin.site.register(Room)

# Add Message
admin.site.register(Message)

