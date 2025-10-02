from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Choice, Test


def index(request):
    """Show list of latest tests"""
    latest_test_list = Test.objects.order_by("-pub_date")[:5]
    context = {"latest_test_list": latest_test_list}
    return render(request, "index.html", context)


def detail(request, test_id):
    """Show a single test with its questions and choices"""
    test = get_object_or_404(Test, pk=test_id)
    return render(request, "detail.html", {"test": test})


def answer(request, test_id):
    """Process submitted answers and redirect to results"""
    test = get_object_or_404(Test, pk=test_id)
    selected_choices = []

    for question in test.question_set.all():
        choice_id = request.POST.get(f"choice_{question.pk}")
        if choice_id:
            try:
                choice = question.choice_set.get(pk=choice_id)
                selected_choices.append(choice)
            except Choice.DoesNotExist:
                pass

    # Calculate score
    total_score = sum(choice.score for choice in selected_choices)

    # Store score in session so results view can access it
    request.session["last_score"] = total_score

    return HttpResponseRedirect(reverse("tests:results", args=(test.id,)))


def results(request, test_id):
    """Show the result page with the computed score"""
    test = get_object_or_404(Test, pk=test_id)
    score = request.session.get("last_score", None)

    return render(request, "results.html", {"test": test, "score": score})
