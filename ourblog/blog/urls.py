from django.urls import path

from . import views

<<<<<<< HEAD
urlpatterns = [
    path('', views.index, name='blog'),
=======
app_name = 'blog'

urlpatterns=[
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ArticleView.as_view(), name='article'),
>>>>>>> 7531963e5667724879b77948df21733b641b9b63
]