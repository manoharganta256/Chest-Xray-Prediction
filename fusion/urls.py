from django.conf.urls import url
from fusion import views
urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^home/',views.home,name='home'),
    url(r'^profile/',views.profile,name='profile'),
    #url(r'^result/',views.result,name='result'),
    #url(r'^login/',views.login),
    #url(r'^profile/',views.update_profile),
    url(r'^accounts/logout/',views.logout_),
    url(r'^delete/',views.delete,name='delete')
]
