from django.shortcuts import render, redirect

from survey.forms import SurveyForm
from survey.models import Question, UserResponse, AnswerOption


def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                if key.startswith('question_'):
                    question_id = int(key.split('_')[1])
                    question = Question.objects.get(id=question_id)
                    if isinstance(value, AnswerOption):
                        UserResponse.objects.create(question=question, selected_answer=value)
                    else:
                        UserResponse.objects.create(question=question, text_answer=value)
            return redirect('thanks')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey.html', {'form': form})


def thanks_view(request):
    return render(request, 'survey/thanks.html')
