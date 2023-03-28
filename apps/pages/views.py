from django.shortcuts import render
from django.views import generic
from apps.pages import forms


class LobbyTemplateView(generic.CreateView):
    template_name = "pages/layout/lobby.html"
    form_class = forms.SessionForm