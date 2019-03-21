from django.db import models

# Create your models here.
class Equipaments(models.Model):

	name=models.CharField('Modelo', max_length=100)
	location=models.TextField('Endereço')

	class Meta:
		verbose_name='Equipamento'
		verbose_name_plural='Equipamentos'
			

	def __str__(self):
		return self.name
		
class Clients(models.Model):
			
    caixa=models.ForeignKey(Equipaments, on_delete=models.CASCADE)
    name=models.CharField('Nome', max_length=100)
    location=models.TextField('Endereço')

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
			

    def __str__(self):
        return self.name

		