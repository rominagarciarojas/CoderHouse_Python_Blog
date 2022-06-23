from pipes import Template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import BlogModel, Contacto
from blogger.models import Avatar
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from blog.forms import ContactoForm, BlogForm


class BlogIndex(TemplateView):
    model = BlogModel
    template_name = 'blog/index.html'
    
class BlogBlogs(ListView):
    model = BlogModel
    template_name = 'blog/blogs.html'

    def get_queryset(self, *args, **kwargs):
        return BlogModel.objects.filter(visible='Público')


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

    def get_context_data(self, **kwargs):
       
        context= super(BlogDetail, self).get_context_data(**kwargs)
        context['blogsPublicos'] = BlogModel.objects.filter(id=self.kwargs['pk'])
        #context['usravatar'] = Avatar.objects.filter(user_id=pk[id])
        context['usravatar'] = Avatar.objects.all()
        return context


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    template_name = 'blog/blogmodel_form.html'
    success_url = reverse_lazy("blog_list")
    form_class= BlogForm

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
    template_name = 'blog/blog_logout.html'
    
    
class BlogContacto(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = "blog/contact.html"
    success_url= reverse_lazy("index")