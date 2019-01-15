from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.post_list,name='post_list'),url('test',views.test,name='test'),url('test',views.doc,name='doc'),url(r'^register/$',views.RegisterFormView.as_view()),]
urlpatterns+=[url(r'^login',views.LoginFormView.as_view()),]
urlpatterns+=[url(r'^logout',views.logout_view),]
urlpatterns+=[url(r'^accounts/logout/',views.logout_view),]
urlpatterns+=[url(r'^zakazy/$',views.zakazy),]
urlpatterns+=[url(r'^shablony/$',views.shablony),]
urlpatterns+=[url(r'update/$',views.update),]
urlpatterns+=[url(r'history/$',views.history),]
urlpatterns+=[url(r'to_shab/$',views.to_shab),]
urlpatterns+=[url(r'create/$',views.create),]
urlpatterns+=[url(r'delete_shab/$',views.delete_shab),]
urlpatterns+=[url(r'names/$',views.names),]