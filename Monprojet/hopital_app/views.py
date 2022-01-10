from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
import hopital_app

from hopital_app.forms import EnfantForm
from .models import Enfant

def home(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'medecines/home.html', {'enfants': enfants})


	

def enfants_list(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'medecines/enfants_list.html', {'enfants': enfants})



def Ajouter_enfant(request):
	submitted = False
	if request.method == "POST":
		form = EnfantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Ajouter_enfant?submitted=True')
	else:
		form = EnfantForm
		if 'submitted' in request.GET:
			submitted=True
		
		



def Editer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	form = EnfantForm(request.POST or None, instance=enfant)
	if form.is_valid():
		form.save()
		return redirect('enfants-list')
	return render(request, 'medecines/editer_enfant',{
			'enfant': enfant,
		'form': form,
	}) 



def supprimer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	enfant.delete()
	return redirect('enfants-list')

def Montrer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	return render(request, 'medecines/montrer_enfant.html', {
		'enfant': enfant,
	})
					
def search_enfant(request):
	if request.method == "GET":
			query = request.GET.get('query')
			if query:
				mutiple_q = Q(Q(nom__icontains=query) | Q(id__icontains=query))
			enfants = Enfant.objects.filter(mutiple_q)
			if enfants:
				return render(request, 'medecines/enfants_list.html', {
					'enfants': enfants
				})
			else:
				print('Not found ...')
				return render(request, 'medecines/introuvable.html', {})
					