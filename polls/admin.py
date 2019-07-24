from django.contrib import admin

from .models import Choice, Question

# Register your models here.

##Tutorial 2
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

##Tutorial 1
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class QuestionAdmin(admin.ModelAdmin):
    ## Tutorial 3
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    ## Tutorial 2
    # fieldsets = [
    #     (None,                  {'fields': ['question_text']}),
    #     ('Date information',    {'fields': ['pub_date']}),
    # ]
    
    ## Tutorial 1
    # fields = ['pub_date', 'question_text']

## Tutorial 1
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)