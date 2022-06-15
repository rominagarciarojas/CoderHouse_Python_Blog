from pipes import Template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
#from CoderHouse_Python_Blog.FinalBlog.blog.models import Contacto
from blog.models import BlogModel, Contacto
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from blog.forms import ContactoForm


class BlogIndex(TemplateView):
    model = BlogModel
    template_name = 'blog/index.html'
    
class BlogBlogs(TemplateView):
    model = BlogModel
    template_name = 'blog/blogs.html'

class BlogAbout(TemplateView):
    model = BlogModel
    template_name = 'blog/about.html'

class BlogContact(TemplateView):
    model = BlogModel
    template_name = 'blog/contact.html'

class BlogTeam(TemplateView):
    model = BlogModel
    template_name = 'blog/team.html'

class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"

    def get_queryset(self, *args, **kwargs):
        return BlogModel.objects.filter(autor=self.request.user)

class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"



class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    #template_name = 'blog/blog_logout.html'
    template_name = 'blog/index.html'
    next_page = reverse_lazy("index")

class BlogContacto(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = "blog/contact.html"
    success_url= reverse_lazy("index")