from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework import routers



router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')



urlpatterns = [

    path('admin/', admin.site.urls),

    # home page route
    path('',views.index, name='home'),

    # route todo query api
    path('api/', include(router.urls)),

    # user registration api route
    path('register/', views.RegisterUserView.as_view()),

    # user login api route
    path('login/', views.LoginUserView.as_view()),

    # user logout api route
    path('logout/', views.logOutUser),


]


