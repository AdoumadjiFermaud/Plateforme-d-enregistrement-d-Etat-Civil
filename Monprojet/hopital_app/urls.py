from django.urls import path
from . import views

urlpatterns = [
		path('', views.home, name='home'),
        path('enfants_list', views.enfants_list, name='enfants-list'),
		path('ajouter_enfant', views.Ajouter_enfant, name='ajouter-enfant'),
		path('editer_enfant/<enfant_id>', views.Editer_enfant, name='editer-enfant'),
		path('supprimer_enfant/<enfant_id>', views.supprimer_enfant, name='supprimer-enfant'),
		path('montrer_enfant/<enfant_id>', views.Montrer_enfant, name='montrer-enfant'),
		path('chercher_enfant', views.search_enfant, name='chercher-enfant'),
	]