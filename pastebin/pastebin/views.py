from django.shortcuts import render, get_object_or_404
from .forms import PasteForm
from .models import Paste


def index(request):
    fields = PasteForm()
    ctx = {'fields': fields}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    ctx = {}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)

def paste_new(request):

    new_paste = Paste.objects.create(
        language=request.POST.get('language'),
        title=request.POST.get('title'),
        content=request.POST.get('content')
    )
    ctx = { 'paste': new_paste }

    return render(request, 'pastebin/paste-detail.jinja2', ctx)
