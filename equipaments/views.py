from django.shortcuts import render

from .models import Equipaments, Clients
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from watson import search as watson
# Create your views here.
class Equipaments(TemplateView):
    template_name = "equipamentos/equipamentos.html"

class EquipamentsList(ListView):
	model = Equipaments
	template_name='equipamentos_list.html'




class ClientsList(ListView):
	model = Clients
	template_name='clientes_list.html'
	
  
class ClientsDetail(DetailView):
	model = Clients
	template_name='clients_detail.html'	

class ClientsCreate(CreateView):
	model = Clients
	template_name='clients_form.html'
	fields = ['Equipamento', 'name', 'location']	
	success_url = reverse_lazy('clients_list')		

class ClientsUpdate(UpdateView):
	model = Clients
	template_name='clients_update_form.html'
	fields = ['caixa', 'name', 'location']	
	success_url = reverse_lazy('clients_list')		

class ClientsDelete(DeleteView):
	model = Clients
	template_name='clients_confirm_delete.html'
	success_url = reverse_lazy('clients_list')			