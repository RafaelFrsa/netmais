from django import forms
from .models import *

class EquipamentForm(forms.ModelForm):

	class Meta:
		model = Equipaments
		fields = ('name', 'location')

class ClientForm(forms.ModelForm):

	class Meta:
		model = Clients
		fields = ('Equipamentos', 'name', 'location')		
