from .forms import NameForm, ContactForm
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse


@permission_required("contacts.add_contact")
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["subject"]
            form.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = ContactForm()
    return render(request, "contacts/create.html", {"form": form})


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name,)))
    else:
        form = NameForm()
    return render(request, "contacts/name.html", {"form": form})


def thanks(request, name):
    return HttpResponse(f"Obrigado por preencher o formulário, {name}")
