from django.contrib import admin

# Register your models here.
from .models import Categorie, Boutique, BoutiqueAdmin, Article, Clients,Produit,Vendeurs,Offre,Utilisateurs,Transaction


admin.site.register(Categorie)
admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Article)
admin.site.register(Clients)
admin.site.register(Produit)
admin.site.register(Vendeurs)
admin.site.register(Offre)
admin.site.register(Utilisateurs)
admin.site.register(Transaction)