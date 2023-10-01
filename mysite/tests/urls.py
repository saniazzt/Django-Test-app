from django.urls import path

from . import views

app_name = "tests"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:test_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:test_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:test_id>/answer/", views.answer, name="answer"),
]