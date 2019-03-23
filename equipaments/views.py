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

###############Clientes#########################################

class EquipamentsList(ListView):
	model = Equipaments
	template_name='equipamentos/equipaments_list.html'

class EquipamentsDetail(DetailView):
	model = Equipaments
	template_name='equipamentos/equipaments_detail.html'


class EquipamentsCreate(CreateView):
	model = Equipaments
	template_name='equipamentos/equipaments_form.html'
	fields = ['name', 'mac', 'bairro', 'rua', 'numero']	

	def get_success_url(self):
		return reverse_lazy('clients_list')


class EquipamentsUpdate(UpdateView):
	model = Equipaments
	template_name='equipamentos/equipaments_update_form.html'
	fields = ['name', 'mac', 'bairro', 'rua', 'numero']	
	
	def get_success_url(self):
		return reverse_lazy('equipaments_list')	

class EquipamentsDelete(DeleteView):
	model = Equipaments
	template_name='equipamentos/equipaments_confirm_delete.html'
	
	def get_success_url(self):
		return reverse_lazy('equipaments_list')


###############Clientes#########################################

class ClientsList(ListView):
	model = Clients
	template_name='clientes/clients_list.html'
	paginate_by = 10

	def get_queryset(self):
		queryset = Clients.objects.all()
		q = self.request.GET.get('q', '')
		if q:
			queryset = watson.filter(queryset, q)
		return queryset

  
class ClientsDetail(DetailView):
	model = Clients
	template_name='clientes/clients_detail.html'


class ClientsCreate(CreateView):
	model = Clients
	template_name='clientes/clients_form.html'
	fields = ['caixa', 'name', 'bairro', 'rua', 'numero', 'planos', 'date']

	def get_success_url(self):
		return reverse_lazy('clients_list')


class ClientsUpdate(UpdateView):
	model = Clients
	template_name='clientes/clients_update_form.html'
	fields = ['caixa', 'name', 'bairro', 'rua', 'numero', 'planos', 'date']
	
	def get_success_url(self):
		return reverse_lazy('clients_list')	

class ClientsDelete(DeleteView):
	model = Clients
	template_name='clientes/clients_confirm_delete.html'
	
	def get_success_url(self):
		return reverse_lazy('clients_list')			