from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add_task,name='add'),
    path('register',views.register,name='register'),
    path('login', views.bogin, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('Edit/<int:id>', views.Edittask, name='edit'),
    path('Delete/<int:id>', views.Deletetask, name='delete')

]
