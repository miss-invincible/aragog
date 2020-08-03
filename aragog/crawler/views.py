from django.shortcuts import render
from .forms import UrlGatherer
from .core import temp


def index(request):
    if request.method == 'POST':
        form = UrlGatherer(request.POST)
        if form.is_valid():
            context = {
                'request': request,
                'valid': form.cleaned_data['url'],
                'data': temp.crawlTheUrl()
            }
            return render(request, 'crawler/output.html', context)
    else:
        form = UrlGatherer()

    context = {
        'form': form,
    }
    return render(request, 'crawler/index.html', context)