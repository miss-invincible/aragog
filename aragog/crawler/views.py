from django.shortcuts import render
from .forms import UrlGatherer


def index(request):
    if request.method == 'POST':
        form = UrlGatherer(request.POST)
        if form.is_valid():
            context = {
                'request': request,
                'valid': form.cleaned_data['url'],
            }
            return render(request, 'crawler/output.html', context)
    else:
        form = UrlGatherer()

    context = {
        'form': form,
    }
    return render(request, 'crawler/index.html', context)