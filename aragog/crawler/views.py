from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if not form.is_valid():
            context = {
                'request': request,
                'valid': form
            }
            return render(request, 'crawler/output.html', context)
    else:
        form = NameForm()

    context = {
        'form': form,
    }
    return render(request, 'crawler/index.html', context)


# def index(request):
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'crawler/index.html', context)
