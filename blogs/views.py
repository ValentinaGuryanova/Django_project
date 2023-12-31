from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.models import Blogs


class BlogsCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    fields = ('title', 'body',)
    success_url = reverse_lazy('blogs:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogsListView(LoginRequiredMixin, ListView):
     model = Blogs

     def get_queryset(self, *args, **kwargs):
         queryset = super().get_queryset(*args, **kwargs)
         queryset = queryset.filter(is_publish=True)
         return queryset


class BlogsDetailView(LoginRequiredMixin, DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class BlogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Blogs
    fields = ('title', 'body',)
    # success_url = reverse_lazy('blogs:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:view', args=[self.kwargs.get('pk')])


class BlogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Blogs
    success_url = reverse_lazy('blogs:list')
