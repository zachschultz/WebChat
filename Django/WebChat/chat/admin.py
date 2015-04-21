from django.contrib import admin
from .models import Message



class MessageAdmin(admin.ModelAdmin):
  fieldssets = [
    (None,    {'fields':['content']}),
    ('Date info.', {'fields': ['post_date'], 'classes':['collapse']})
  ]

admin.site.register(Message, MessageAdmin)


# Register your models here.
