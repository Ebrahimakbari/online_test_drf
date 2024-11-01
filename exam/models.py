from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self) -> str:
        return self.title
    
    
class FavoriteCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='favorites')
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='favorite_category')
    
    def __str__(self) -> str:
        return self.category.title
    
class Exam(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    duration = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='exams')
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='exams')

    def __str__(self) -> str:
        return self.title


class Participation(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, related_name = 'participations')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'participations')
    participate_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        unique_together = ('exam', 'student')
    
    def __str__(self) -> str:
        return self.exam.title + ' - ' + self.student.full_name()
    
class Question(models.Model):
    question_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='questions')
    
    def __str__(self) -> str:
        return self.question_text

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length = 100)
    is_correct_answer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.option_text
    
class Answer(models.Model):
    selected_option = models.ForeignKey(QuestionOption, on_delete=models.PROTECT, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='answers')
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    
    class Meta:
        unique_together = ('question', 'student')
        
    def __str__(self) -> str:
        return self.selected_option.option_text

class Score(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, related_name='scores')
    score = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    
    def __str__(self) -> str:
        return self.student.full_name() + ' - ' + self.exam.title