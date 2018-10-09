from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.text import Truncator
from django.urls import reverse 

# Create your models here.
class Category(models.Model):
    nom = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.nom    

    def get_absolute_url(self):
        return reverse('ahnata:article_list_by_category', args=[self.slug])

class Boutique(models.Model):
    """docstring for ClassName"""
    nom = models.CharField(max_length=25)
    stock_gerant = models.CharField(max_length=30)
    categorie = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now, verbose_name="date d'ajout")
  
    def get_absolute_url(self):
        return reverse('ahnata:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nom + ' - ' + self.stock_gerant   

class Articles(models.Model):
    """docstring for ClassName"""
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    nom = models.CharField(max_length=45, db_index=True)
    slug = models.SlugField(max_length=45, db_index=True)
    prix = models.FloatField()
    description = models.CharField(max_length=100)
    article_logo = models.ImageField(upload_to='ahnata/%Y/%m/%d', blank=True)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(default=timezone.now, verbose_name="date d'ajout")
    date_modif = models.DateTimeField(default=timezone.now, verbose_name="date de modification")
   
    def get_absolute_url(self):
        return reverse('ahnata:detail_art', kwargs={'pk': self.pk})
 
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
    nom = models.CharField(max_length=30, db_index=True)  
   
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

class Post(models.Model):
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre
        
