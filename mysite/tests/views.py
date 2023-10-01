from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import render, get_object_or_404


from .models import Choice, Test,Question


def index(request):
    latest_test_list = Test.objects.order_by("-pub_date")[:5]
    context = {"latest_test_list": latest_test_list}
    return render(request, "tests/index.html", context)


def detail(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "tests/detail.html", {"test": test})
#    return HttpResponse("You're looking at test %s." % test_id)


def results(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render(request, "tests/results.html", {"test": test})



def answer(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    selected_choice = []

    # question1 = test.question_set.get(pk=1)
    # question2 = test.question_set.get(pk=2)
    for question in test.question_set.all():
        try:
            selected_choice1 = question.choice_set.get(pk=request.POST["choice_{}".format(question.pk)])
            # selected_choice2 = question2.choice_set.get(pk=request.POST["choice_2"])
            selected_choice.append( selected_choice1 )
            
        except (KeyError, Choice.DoesNotExist):
            pass
            # # Redisplay the question voting form.
            # return render(
            #     request,
            #     "tests/detail.html",
            #     {
            #         "test": test,
            #         "error_message": "You didn't select a choice.",
            #     },
            # )

        # selected_choice1.save()
        # selected_choice2.save()
        # selected_choice [0].save()
    test.total_score = 0
    test.save()    
    for choice in selected_choice:
        test.total_score += choice.score
        test.save()
    return HttpResponseRedirect(reverse("tests:results", args=(test.id,)))
#    return HttpResponse("You're answering test %s" % test_id , "question %s." % question_id)