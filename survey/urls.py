from django.urls import path

from survey.views import survey_view, thanks_view, feedback_view

urlpatterns = [
    path('', survey_view, name='survey'),
    path('thanks/', thanks_view, name='thanks'),
    path('feedback/', feedback_view, name='feedback'),
]