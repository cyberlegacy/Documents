from django.urls import path
from . import views

app_name = 'japanese_class_app'  # Namespace for URLs

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('levels/', views.levels_view, name='levels'),
    path('level-assessment/', views.level_assessment_view, name='level_assessment'),
    path('signup/', views.signup_page_view, name='signup'),
    path('contact/', views.contact_view, name='contact'),
    
    # API endpoint
    path('api/signup/', views.api_signup_view, name='api_signup'),
]
