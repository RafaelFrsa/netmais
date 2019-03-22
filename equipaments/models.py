from django.db import models

# Create your models here.
class Equipaments(models.Model):

	name=models.CharField('Modelo', max_length=100)
	mac=models.CharField('Mac', max_length=10)
	bairro=models.CharField('Bairro', max_length=100)
	rua=models.CharField('Rua', max_length=100)
	numero=models.CharField('Nº', max_length=10)


	class Meta:
		verbose_name='Equipamento'
		verbose_name_plural='Equipamentos'
			

	def __str__(self):
		return self.name
		
class Clients(models.Model):

	PLANOS = (
   		 ('3MB', '3MB'),
    	 ('5MB', '5MB'),
		 ('10MB', '10MB'),
		 ('15MB', '15MB'),
		 ('20MB', '20MB'),
		 ('25MB', '25MB'),
		 ('50MB', '50MB'),
	)
			
	caixa=models.ForeignKey(Equipaments, on_delete=models.CASCADE)
	name=models.CharField('Nome', max_length=100)
	bairro=models.CharField('Bairro', max_length=100)
	rua=models.CharField('Rua', max_length=100)
	numero=models.CharField('Nº', max_length=10)
	planos = models.CharField(max_length=5, choices=PLANOS)
	date = models.DateField('Data')

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
			

	def __str__(self):
		return self.name

		