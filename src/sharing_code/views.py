from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import SnippetForm
from .models import Snippet
from django.views.generic import DetailView, FormView

"""def createSnippet(request):
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
"""


class CreateSnippet(FormView):
    form_class = SnippetForm
    template_name = 'createSnippet.html'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            snippet = form.save(commit=False)
            snippet.save()
            return HttpResponseRedirect(reverse('snippet:detail', kwargs={'pk': snippet.id}), self.get_context_data())
        return render(self.request, 'createSnippet.html', self.get_context_data())


class ViewSnippet(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'viewSnippet.html'
