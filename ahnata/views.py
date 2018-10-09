from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from django import forms
from .models import Boutique, Articles, Category
from .forms import signUpForm, ContactForm, LoginForm, PostForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ahnata/index.html'

    def get_queryset(self):
        #return all boutiques 
        return Boutique.objects.all() 

# Create your views here.
class LayoutView(generic.ListView):
    template_name = 'ahnata/layout.html'
    context_object_name = 'all_boutiques'

    def get_queryset(self):
        #return all boutiques 
        return Boutique.objects.all()        

class ArticlelistView(generic.ListView):
    template_name = 'ahnata/list.html'
    context_object_name = 'all_articles'
    
    def get_queryset(self):
        return Articles.objects.all()

class DetailArticleView(generic.DetailView):
    """affciher un article au complet"""    
    model = Articles
    template_name = 'ahnata/detail_art.html'      

class DescripView(TemplateView):
    """affciher une Boutique au complet"""	
    template_name = 'ahnata/descript.html'     	  

class signUpFormView(View):
    form_class = signUpForm
    template_name = 'ahnata/register.html' 
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    # process form data 
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
           
            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('ahnata:index')     
        return render(request, self.template_name, {'form': form})   


def emailView(request):
    template_name = 'ahnata/contact.html'
    
    if request.method =='GET':
        form = ContactForm()
    else:    
        form = ContactForm(request.POST)
        if form.is_valid():

            #cleaned (normalized) data
            sujet = form.cleaned_data['sujet']
            emailAdress = form.cleaned_data['emailAdress']
            message = form.cleaned_data['message']
            
            receveur = ['foulaly2018@gmail.com']
            if sujet and message and emailAdress:
                try:
                    send_mail(sujet, message, emailAdress, 
                        receveur,fail_silently=False,)
                except BadHeaderError :
                    return HttpResponse('Invalid header found')
                return redirect('ahnata:success')
            else:
                return HttpResponse('make sure all fields are entered and valid')   
                   
    return render(request, template_name, {'form':form})

def successView(request):
    return render(request,'ahnata/success.html')

def post_new(request):
    template_name = 'ahnata/post_edit.html'

    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try:
                post.auteur = request.user
            except BadHeaderError :
                return HttpResponse('Vous devez etre connecter')
            post.date_publication = timezone.now()
            post.save() 
            return redirect('ahnata:detail_art', pk=post.pk)      
    return render(request, template_name, {'form': form})    