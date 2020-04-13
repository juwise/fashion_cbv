from django.conf.urls import url
from anoapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'anoapp'
urlpatterns = [
    url(r'^$',views.FashionListView.as_view(), name='list'),
    url(r'^latest',views.LatestTemplateView.as_view(), name='latest'),
    url(r'^about/',views.about, name='about'),
    url(r'^create',views.FashionCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[-\w]+)/$',views.FashionDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[-\w]+)/$',views.FashionUpdateView.as_view(),name='update'),
    url(r'^register',views.registers,name='registers'),
    url(r'^login',views.login_page, name='login'),
    url(r'^logout',views.logout, name='logout'),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
