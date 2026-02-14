1) Créer le module:
python3 -m venv venv

2) Activer:
venv\Scripts\activate

3)Installer:
python -m pip install Django

5) Le projet:
django-admin startproject nom_projet .

6) L'application:
 django-admin startapp nom_app
django-admin startapp bibliotheque


7)Mettre le nom de l'application dans Installed Apps de settings

8) Faire un:
def accueil(request):
    return HttpResponse("<h1>Yo</h1>")

dans views.py du nom_app

9) Ajouter la route dans l'URL:
dans urls.py de nom_projet

10) Tester avec python manage.py runserver

11) Créer la classe du modèle dans models.py de nom_app

12) Faire python manage.py makemigrations pour créer la migration
