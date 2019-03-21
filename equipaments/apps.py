from django.apps import AppConfig
from watson import search as watson


class EquipamentsConfig(AppConfig):
    name = 'equipaments'
    verbose_name = 'Equipamentos'

    def ready(self):
    	Clients = self.get_model('Clients')
    	watson.register(Clients)