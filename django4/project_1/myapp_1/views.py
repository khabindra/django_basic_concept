# views.py
from django.shortcuts import render, redirect
from .forms import BlogPostForm

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Save the form data as a new BlogPost instance
            new_post = form.save()
            return redirect('blog_post_detail', pk=new_post.pk)
    else:
        form = BlogPostForm()

    return render(request, 'home.html', {'form': form})
