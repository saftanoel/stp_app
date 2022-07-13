from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from statii.models import Statie, Autobuz


def index(request):
    return HttpResponse("Bine ai venit pe site-ul STP. Statii")


class StatiiView(ListView):
    template_name = "statii.html"
    model = Statie

    def get_context_data(self, **kwargs):
        context = super(StatiiView, self).get_context_data(**kwargs)
        Autobuze = Autobuz.objects.all()
        context.update({"autobuze": Autobuze})
        return context


