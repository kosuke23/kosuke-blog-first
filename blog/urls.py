from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('post/new/', views.CreateView.as_view(), name='post_new'),
    path('post/<int:pk>', views.UpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', views.delete, name='delete'),
]

#    path('post/new/', views.post_new, name='post_new'),
#    path('post/<int:pk>', views.post_edit, name='post_edit'),
#    path('post/delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
#    path('drafts/', views.post_draft_list, name='post_draft_list'),
#    path('login/', views.Login.as_view(), name='login'),
#    path('logout/', views.Logout.as_view(), name='logout'),

