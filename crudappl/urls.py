from django.conf.urls import url
from crudappl import views 

urlpatterns = [ 
     url(r'^api/crudappl$',views.user_list),
     url(r'^api/crudappl/(?P<pk>[0-9]+)$', views.user_detail),
  
    ]
    