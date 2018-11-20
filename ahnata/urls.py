from django.conf.urls import url
from django.contrib.auth import views as auth_views 
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path


from . import views

app_name ='ahnata'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name ='ahnata/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'ahnata/logout.html'), name='logout'),
    url(r'^layout/$', views.LayoutView.as_view(), name='layout'),
    url(r'^register/$', views.signUpFormView.as_view(), name='register'),
    url(r'^descript/$', views.DescripView.as_view(), name='descript'),
    url(r'^articles/$', views.ArticlelistView.as_view(), name='articles'),
    url(r'^detail_art/(?P<pk>\d+)/$', views.DetailArticleView.as_view(), name='detail_art'),
    path('contact/', views.emailView, name='contact'),
    path('success/', views.successView, name='success'),
    #url(r'^list_post/$', views.post_list, name='post_list'),
    #url(r'^post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/$', views.post_new, name='post'),

]
