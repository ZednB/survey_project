from django import forms

from survey.models import Question, AnswerOption


class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            if question.has_text_answer:
                self.fields[f"question_{question.id}"] = forms.CharField(
                    label=question.text,
                    widget=forms.Textarea,
                    required=False
                )
            else:
                answer_options = AnswerOption.objects.filter(question=question)
                self.fields[f"question_{question.id}"] = forms.ModelChoiceField(
                    label=question.text,
                    queryset=answer_options,
                    widget=forms.RadioSelect,
                    required=False
                )
