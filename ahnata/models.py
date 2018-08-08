from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.text import Truncator
from django.urls import reverse 

# Create your models here.
class Categorie(models.Model):

    nom = models.CharField(max_length=30)

    def __str__(self):

        return self.nom

class Boutique(models.Model):
    """docstring for ClassName"""
    nom = models.CharField(max_length=25)
    stock_gerant = models.CharField(max_length=30)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now, verbose_name="date d'ajout")
  
    def get_absolute_url(sel):
        return reverse('ahnata:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nom + ' - ' + self.stock_gerant   

class Article(models.Model):
    """docstring for ClassName"""
    nom = models.CharField(max_length=25)
    prix = models.FloatField()
    description = models.CharField(max_length=30)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    article_logo = models.CharField(max_length=1000)
    date_ajout = models.DateTimeField(default=timezone.now, verbose_name="date d'ajout")

    def __str__(self):
        return self.nom   

class Clients(models.Model):
    
    nom = models.CharField(max_length=25)
    adresse = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        
        return self.nom
class Produit(models.Model):
    nom = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom    

class Vendeurs(models.Model):
    
    nom = models.CharField(max_length=25)
    adresse = models.CharField(max_length=20)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    produits = models.ManyToManyField(Produit, through='Offre',related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")#permet d'associer +sieurs produits à un vendeur et vice-versa

    def __str__(self):
        return self.nom  

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeurs, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)


class Utilisateurs(models.Model):
    
    nom = models.CharField(max_length=25)
    adresse = models.CharField(max_length=20)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    
    """class Meta:
    	
    	verbose_name="clients"""

    def __str__(self):
        
        return self.nom 

class Transaction(models.Model):

    c_id = models.IntegerField(blank=True, null=True)
    a_id = models.IntegerField(blank=True, null=True)
                		        
    def __str__(self):
                    		        	
        return self.c_id        		        		                		        

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
        
    """ def apercu_descrip(self, article):

        return Truncator(article.categorie).chars(5, truncate='')

    # En-tête de notre colonne

    apercu_descrip.short_description = 'categorie'  """       
        
                                      
                        		