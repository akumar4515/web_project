from django.contrib import admin
from .models import UserProfile, Message, Courses,Topic,Sub_topic,contents
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Courses)
admin.site.register(Topic)
admin.site.register(Sub_topic)
admin.site.register(contents)

