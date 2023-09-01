from django.shortcuts import render, redirect, reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def index(request):
	title = request.GET.get('query')
	if title:
		advertisements = Advertisement.objects.filter(title=title)
	else:
		advertisements = Advertisement.objects.all()
	context = {
		'advertisements' : advertisements,
		'title': title
	}
	return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
	return render(request, 'app_advertisement/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
	if request.method == 'POST':
		form =AdvertisementForm(request.POST, request.FILES)
		if form.is_valid():
			#advertisement = Advertisement(**form.cleaned_data)
			advertisement = form.save(commit=False)
			advertisement.user = request.user
			advertisement.save()
			return redirect(reverse('main_page'))
	else:
		form = AdvertisementForm()
	context = {'form': form}
	return render(request, 'app_advertisement/advertisement-post.html', context)
