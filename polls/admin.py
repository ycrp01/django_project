from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    
    inlines = [ChoiceInline] # Choice model class 같이 보기
    list_display = ('question_text','pub_date','was_published_recently') # record list column 지정

    list_filter = ['pub_date'] # filter side-bar 추가
    search_fields = ['question_text'] # search-box 추가

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)