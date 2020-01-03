from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from .forms import ListCreateForm
from .models import List

class ListHome(TemplateView):
    template_name = 'list/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ListDetailView(DetailView):
    model = List

class AllListView(ListView):
    model = List
    template_name = 'list/list.html'

class ListCreateView(CreateView):
    model = List
    form_class = ListCreateForm
    template_name = 'list/create.html'
    permission_required='list.add_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание вашего списка дел:"
        return context
    def get_success_url(self):
        user = self.request.user
        self.object.user = user
        self.object.save()
        return '/list/alllist'

class ListUpdateView(UpdateView):
    model = List
    form_class = ListCreateForm 
    template_name = 'list/create.html'
    permission_required='list.change_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование вашего списка дел:"
        return context

class ListDeleteView(DeleteView):
    model = List
    template_name = 'list/delete.html'
    success_url = '/list/alllist'
    permission_required='list.delete_list'
