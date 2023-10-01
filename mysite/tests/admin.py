from django.contrib import admin

from .models import Test,Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": [], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3    
    

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["test_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
