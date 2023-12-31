from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()

class Advertisement(models.Model):
	title =models.CharField(verbose_name='Название', max_length=128)
	description =models.TextField('Описание')
	price =models.DecimalField('Цена', max_digits=10, decimal_places=2)
	auction =models.BooleanField('Торг', help_text='Отемтьте если торг уместен')
	created_at =models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	image =models.ImageField('изображение', upload_to='advertisements/')

	@admin.display(description='дата создания')
	def created_date(self):
		if self.created_at.date()==timezone.now().date():
			created_time=self.created_at.time().strftime('%H:%M:%S')
			return format_html(
				'<span style="color: green; font-weight:bold;">Сегодня в {}</span>',created_time
			)
		return self.created_at.strftime('%d,%m,%Y')

	@admin.display(description='обновлено')
	def update_date(self):
		if self.update_at.date() == timezone.now().date():
			update_time = self.update_at.time().strftime('%H:%M:%S')
			return format_html(
				'<span style="color: blue; font-style:italic;">Сегодня в {}</span>', update_time
			)
		return self.update_at.strftime('%d,%m,%Y')

	@admin.display(description='изображение')
	def get_html_image(self):
		if self.image:
			return format_html(
				'<img src="{url}" style="max-width: 50px; max-height: 50px;">', url=self.image.url
			)

	def __str__(self):
		return f"Advertisement({self.id}, {self.title}, {self.price}"

	class Meta:
		db_table = "advertisements"

	def get_url(self):
		return reverse('adv-detail', kwargs={'pk': self.pk})
