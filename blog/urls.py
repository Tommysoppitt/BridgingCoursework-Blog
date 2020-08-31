from django.urls import path
from . import views
urlpatterns = [
path('', views.post_list, name='post_list'),
path('post/<int:pk>/', views.post_detail, name='post_detail'), 
path('post/new/', views.post_new, name='post_new'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
path('cv', views.cv, name='cv'),
path('cv/skill_new', views.skill_new, name='skill_new'),
path('cv/experience_new', views.experience_new, name='experience_new'),
path('cv/responsibility_new', views.responsibility_new, name='responsibility_new'),
path('cv/hobby_new', views.hobby_new, name='hobby_new'),
]
