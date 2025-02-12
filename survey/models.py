from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст вопроса')
    has_text_answer = models.BooleanField(default=False, verbose_name='Текстовый ответ')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(max_length=255, verbose_name='Текст варианта ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    selected_answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name='Выбранный ответ')
    text_answer = models.TextField(blank=True, null=True, verbose_name='Текстовый ответ')

    def __str__(self):
        if self.selected_answer:
            return f"Ответ на вопрос {self.question.text}: {self.selected_answer.text}"
        else:
            return f"Ответ на вопрос {self.question.text}: {self.text_answer}"

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
