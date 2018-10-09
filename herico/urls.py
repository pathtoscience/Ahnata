from django.conf.urls import url


from . import views 
 
app_name = 'herico'
urlpatterns = [
             url('', views.index, name='index')
 ]