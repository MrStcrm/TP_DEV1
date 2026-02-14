from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from gestionApp.models import Categorie, Produit

def accueil(request):
    return render(request, 'home.html')

def liste_produits(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def detail_produit(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    return render(request, 'detailProduit.html', {'produit': produit})

def detail_categorie(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)
    return render(request, 'categorie_detail.html', {'categorie': categorie})

def ajouter_produit(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        categorie_id = request.POST['categorie']
        categorie = Categorie.objects.get(id=categorie_id)
        Produit.objects.create(nom=nom, description=description, prix=prix, categorie=categorie)
        return redirect('liste_produits')
    categories = Categorie.objects.all()
    return render(request, 'ajoutProduit.html', {'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        description = request.POST['description']
        Categorie.objects.create(nom=nom, description=description)
        return redirect('liste_categories')
    return render(request, 'ajoutCategorie.html')

def modifier_produit(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    if request.method == 'POST':
        produit.nom = request.POST['nom']
        produit.description = request.POST['description']
        produit.prix = request.POST['prix']
        categorie_id = request.POST['categorie']
        produit.categorie = Categorie.objects.get(id=categorie_id)
        produit.save()
        return redirect('liste_produits')
    categories = Categorie.objects.all()
    return render(request, 'modifProduit.html', {'produit': produit, 'categories': categories})

def modifier_categorie(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)
    if request.method == 'POST':
        categorie.nom = request.POST['nom']
        categorie.description = request.POST['description']
        categorie.save()
        return redirect('liste_categories')
    return render(request, 'modifCategorie.html', {'categorie': categorie})

def supprimer_produit(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    produit.delete()
    return redirect('liste_produits')

def supprimer_categorie(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)
    categorie.delete()
    return redirect('liste_categories')

def rechercher_produit(request):
    query = request.GET.get('q')
    produits = Produit.objects.filter(nom__icontains=query)
    return render(request, 'rechercher_produit.html', {'produits': produits, 'query': query})
