from django.contrib import admin

from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
	list_display = ['id','title','description','price', 'auction', 'created_date','update_date']
	list_filter = ['auction', 'created_at']
	actions = ['make_auction_as_false','make_auction_as_true']
	fieldsets = (
		('Общий', {
			'fields' : ('title','description')
		}),
		('Финансы', {
			'fields': ('price', 'auction'),
			'classes':['wide', 'extragretty']
		})
	)

	@admin.action(description='убрать торг')
	def make_auction_as_false(self, request, queryset):
		queryset.update(auction=False)

	@admin.action(description='поставить торг')
	def make_auction_as_true(self, request, queryset):
		queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
