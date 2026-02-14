"""
URL configuration for Monprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name='accueil'),

    path("produits/", liste_produits, name="liste_produits"),
    path("produits/ajouter/", ajouter_produit, name="ajoutProduit"),
    path("produits/modifier/<int:produit_id>/", modifier_produit, name="modifProduit"),
    path("produits/supprimer/<int:produit_id>/", supprimer_produit, name="supprProduit"),
    path("produits/<int:produit_id>/", detail_produit, name="detailProduit"),
    path("produits/rechercher/", rechercher_produit, name="rechercherProduit"),


    path("categories/", liste_categories, name="liste_categories"),
    path("categories/ajouter/", ajouter_categorie, name="ajoutCategorie"),
    path("categories/modifier/<int:categorie_id>/", modifier_categorie, name="modifCategorie"),
    path("categories/supprimer/<int:categorie_id>/", supprimer_categorie, name="supprCategorie"),
    path("categories/<int:categorie_id>/", detail_categorie, name="detailCategorie"),
]

