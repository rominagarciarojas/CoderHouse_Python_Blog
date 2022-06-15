from django.urls import path
from blog import views

urlpatterns = [
    path("index/", views.BlogIndex.as_view(), name="index"),  
    path("about/", views.BlogAbout.as_view(), name="about"),
    path("contact/", views.BlogContact.as_view(), name="contact"),
    path("team/", views.BlogTeam.as_view(), name="team"),
    path("lista/", views.BlogList.as_view(), name="blog_list"),
    path("crear/", views.BlogCreate.as_view(), name="blog_create"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    path("entrar/", views.BlogLogin.as_view(), name="blog_login"),
    path("salir/", views.BlogLogout.as_view(), name="blog_logout"),
    path("blogs/", views.BlogBlogs.as_view(), name="blogs"),    
]