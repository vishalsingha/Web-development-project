from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'spiciyo-home'),
    path('about/', views.about, name = 'spiciyo-about'),
    path('contact/', views.contact, name = 'spiciyo-contact'),
    path('blog/', views.blog, name = 'spiciyo-blog'),
    path('recipe/', views.recipe, name = 'spiciyo-recipe'),
    path('info_s', views.call_request, name = 'spiciyo-home_info'),
    path('about/info_s', views.call_request, name = 'spiciyo-about_info'),
    path('contact/info_s', views.call_request, name = 'spiciyo-contact_info'),
    path('blog/info_s', views.call_request, name = 'spiciyo-blog_info'),
    path('recipe/info_s', views.call_request, name = 'spiciyo-recipe_info'),
    path('subscribe', views.subscribe, name = 'spiciyo-home_subscribe'),
    path('about/subscribe', views.subscribe, name = 'spiciyo-about_subscribe'),
    path('contact/subscribe', views.subscribe, name = 'spiciyo-contact_subscribe'),
    path('blog/subscribe', views.subscribe, name = 'spiciyo-blog_subscribe'),
    path('recipe/subscribe', views.subscribe, name = 'spiciyo-recipe_subscribe'),
   
]
