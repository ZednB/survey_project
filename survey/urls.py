from django.urls import path

from survey.views import survey_view, thanks_view

urlpatterns = [
    path('', survey_view, name='survey'),
    path('thanks/', thanks_view, name='thanks'),
]