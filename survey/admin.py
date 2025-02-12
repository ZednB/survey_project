from django.contrib import admin

from survey.models import Question, AnswerOption, UserResponse

# admin.site.register(Question)
# admin.site.register(AnswerOption)
# admin.site.register(UserResponse)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'has_text_answer')
    search_fields = ('text',)
    list_filter = ('has_text_answer',)

@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')
    search_fields = ('text',)
    list_filter = ('question',)

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'selected_answer', 'text_answer')
    search_fields = ('question__text', 'text_answer')
    list_filter = ('question',)
