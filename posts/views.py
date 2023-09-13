from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required(login_url='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.author = request.user
            post.save()
            return redirect('home')

    else:
        form = PostForm()

    context = {
        "form": form
    }

    return render(request, 'posts/create.html', context)
