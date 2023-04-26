from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from datetime import datetime
from .filters import NewsFilter
from .forms import CreateNewsForm

class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'mainnews.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Textnews(DetailView):
    model = Post
    template_name = 'textnews.html'
    context_object_name = 'post'


class CreateNews(CreateView):
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType= 'NW'
        return super().form_valid(form)


class UpdateNews(UpdateView):
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'


class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url= reverse_lazy('News_list')

class ArticlesCreate(CreateView):
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType= 'AR'
        return super().form_valid(form)


class UpdateArticles(UpdateView):
    form_class = CreateNewsForm
    model = Post
    template_name = 'news_edit.html'


class DeleteArticles(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('News_list')