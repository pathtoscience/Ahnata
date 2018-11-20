from django.contrib import admin

# Register your models here.
from .models import Category, Boutique, Articles, Clients,Produit,Vendeurs,Offre,Utilisateurs,Transaction
from .models import Post
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nom','slug']
    prepopulated_fields = {'slug':('nom',)}
admin.site.register(Category, CategoryAdmin)
class BoutiqueAdmin(admin.ModelAdmin):
    list_display = ('nom','stock_gerant','categorie')
    list_filter = ('stock_gerant','date_create')
    date_hierarchy = 'date_create'
    ordering = ('date_create',)
    search_fields = ('nom', 'categorie') 

        # Configuration du formulaire d'édition
    fieldsets = (

        # Fieldset 1 : meta-info (titre, auteur…)

       ('Général', {

            'classes': ['collapse', ],

            'fields': ('nom','stock_gerant')

        }),

        # Fieldset 2 : contenu de l'article

        ('Contenu de la Boutique', {

           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',

           'fields': ('categorie', )

        }),

    )

    # Colonnes personnalisées 

    def apercu_descrip(self, article):

        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il

        y a plus de 40 caractères, il faut rajouter des points de suspension.

        """
        text = article.categorie[0:7]

        if len(article.categorie) > 7:

            return '%s…' % text

        else:

            return text

    apercu_descrip.short_description = 'aperçu du contenu'                
admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Produit)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug','category', 'prix', 'stock','disponible', 'date_ajout', 'date_modif']
    list_filter =['disponible','date_ajout','date_modif','category']
    list_editable = ['prix', 'stock', 'disponible']
    prepopulated_fields = {'slug':('nom',)}
admin.site.register(Articles, ArticleAdmin)
admin.site.register(Clients)
admin.site.register(Vendeurs)
admin.site.register(Offre)
admin.site.register(Utilisateurs)
admin.site.register(Transaction)
admin.site.register(Post)
