from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^upload/', views.upload_hood, name='upload'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^accounts/update/', views.edit, name='update_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^hood/(?P<hood_id>\d+)', views.hood, name='hood'),
    url(r'^join(?P<hood_id>\d+)', views.join, name='join'),
    url(r'^leave/(?P<hood_id>\d+)', views.leave, name='leave'),
    url(r'^upload_business/', views.upload_business, name='upload_business'),
    url(r'^post/', views.add_post, name='post'),
    path('registration_form/', views.signup, name='signup'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)