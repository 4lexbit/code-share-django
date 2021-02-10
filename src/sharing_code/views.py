from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import SnippetForm
from .models import Snippet
from django.views.generic import DetailView, FormView


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
