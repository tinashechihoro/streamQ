from django.contrib import admin
from .models import Profile
from questions.models import Comment,Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']




admin.site.register(Profile, ProfileAdmin)
admin.site.register(Question)
admin.site.register(Comment, CommentAdmin)
