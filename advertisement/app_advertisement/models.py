from django.db import models

class Advertisement(models.Model):
	title =models.CharField(verbose_name='Название', max_length=128)
	description =models.TextField('Описание')
	price =models.DecimalField('Цена', max_digits=10, decimal_places=2)
	auction =models.BooleanField('Торг', help_text='Отемтьте если торг уместен')
	created_at =models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Advertisement({self.id}, {self.title}, {self.price}"

	class Meta:
		db_table = "advertisements"


