"""
URL configuration for studentManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vegies.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


handler404 = 'home.views.handler404'
urlpatterns = [
    
    path('home/',home),
    path('success-page/',success_page,name="success_page"),
    path('voting/', voting, name="voting"),
    path('records/',studentRecord , name="studentRecord"),
    
    # ---------------------------------
    path('index/', index, name="index"),
    path('stu/', viewStudent, name="viewStudent"),
    path('vote/', viewVoting, name = "viewVoting"),
    
    # ---------------practice--------------------------------
    # path('', main, name="main"),
    path('display/',displayData, name="displayData"),
    path('details/<int:id>', detailsMore, name="displayMore"),
    # -----------------------------------------------------
    
   
    # --------------------------------
    path('',register_page, name="register_page"),
    path('recipes/', recipes, name="recipes"),
    path('show_recipe/',show_recipe, name="show_recipe"),
    path('delete_Recipe/<id>/', delete_Recipe, name="delete_Recipe"),
    path('update_Recipe/<id>/', update_Recipe, name="update_Recipe"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/',log_out, name="log_out"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


