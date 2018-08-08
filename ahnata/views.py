from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.views import generic
from django.core.mail import send_mail
from django.views.generic import View, TemplateView

from django import forms
from .models import Boutique, Article
from .forms import UserForm, ContactForm
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ahnata/index.html'
    context_object_name = 'all_boutiques'

    def get_queryset(self):
        #return all articles 
        return Boutique.objects.all() 

class DetailView(generic.DetailView):
    """affciher un article au complet"""	
    model = Boutique
    template_name = 'ahnata/detail.html'     	

class BoutiqueCreate(CreateView):
    model =Boutique
    fields = ['nom', 'prix', 'description', 'categorie']

class BoutiqueUpdate(UpdateView):
    model = Boutique
    fields = ['nom', 'prix', 'description', 'categorie']
        
class BoutiqueDelete(DeleteView):
    model = Boutique
    success_url = reverse_lazy('ahnata:index')

class UserFormView(View):
    form_class = UserForm
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

class ContactView(TemplateView):
    template_name = 'ahnata/contact.html'
    
    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form':form})
        
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():

            #cleaned (normalized) data
            sujet = form.cleaned_data['sujet']
            emailAdress = form.cleaned_data['emailAdress']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            receveur = [foulaly2018@gmail.com]
            if cc_myself:
                receveur.append(emailAdress)

            send_mail(sujet, emailAdress, message, receveur)    
            #returns user objects if credentials are correct
            envoi=True
            form = ContactForm()
            return redirect('ahnata:index')   
                  
        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)

