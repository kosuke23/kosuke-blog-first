from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from .forms import  PostForm
from .models import Post
# Create your views here.


class IndexView(generic.ListView):
    model = Post
    ordering = '-published_date'
    paginate_by = 5


class DetailView(generic.DetailView):
    model = Post


class CreateView(generic.CreateView):
    model = Post
    fields = ['title', 'text', 'images']
    #form_class = PostForm
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('blog:list')
#    success_url = reverse_lazy('blog:list')


class UpdateView(generic.UpdateView):
    model = Post
    fields = ['title', 'text', 'images']
    #form_class = PostForm
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('blog:list')
    # success_url = reverse_lazy('blog:list')


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:list')



"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
           # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


class DeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

"""