from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

@admin.register(models.FavoriteCategory)
class FavoriteCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'student')

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'category', 'created','instructor')
    
@admin.register(models.Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('student', 'participate_at','expires_at')

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('created',)
    
@admin.register(models.QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('created', 'is_correct_answer')

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('created', 'student')
    
@admin.register(models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'student','created')