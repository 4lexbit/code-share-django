from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import SnippetForm
from .models import Snippet
from django.views.generic import DetailView, ListView


def createSnippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=True)
            snippet.save()
            return HttpResponseRedirect(reverse('snippet:detail', kwargs={'pk': snippet.id}))
    else:
        form = SnippetForm()
    context = {'form': form}
    return render(request, 'createSnippet.html', context)


class ViewSnippet(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'viewSnippet.html'
