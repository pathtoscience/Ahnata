from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

app_name ='ahnata'
urlpatterns = [
    
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^contact/$',views.ContactView.as_view(), name='contact'),
    #url(r'^login/$', views.UserFormView.as_view(), name='login')
    #url(r'^logout/$', views.logoutView.as_view(), {'next_page': 'ahnata:login'}, name='logout')


]