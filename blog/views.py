from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Comment


def blogIndex(request):
    posts = Post.objects.all().order_by("-createdOn")
    context = {"posts": posts}
    return render(request, "blogIndex.html", context)


def blogCategory(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-createdOn"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blogCategory.html", context)


def blogDetails(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blogDetails.html", context)