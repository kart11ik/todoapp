from django.urls import path

from . import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView, CustomLogin

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('task-list', TaskList.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task-view/<int:pk>', TaskDetailView.as_view(), name='task-view'),
    # path('login', CustomLoginView.as_view(), name='login')
    #path('login', views.login_fun, name='login'),
    #path('register', views.register_fun, name='register')
    #path('',views.Home, name='home')
]
