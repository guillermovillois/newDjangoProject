from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm

# CRUD
# GET (RETRIEVE / LIST)
# POST (CREATE/UPDATE/DELETE)


def blog_post_list_view(request):
    # obj = get_object_or_404(BlogPost, slug=slug) #reemplaza a lo de abajo...
    # try:
    #     obj = BlogPost.objects.get(id=post_id)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list':qs}
    return render(request, template_name,context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'object_list': obj}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {'object': obj}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None)
    # print(form.cleaned_data)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request, template_name, context)


# def blog_post_create_view(request):
#     form = BlogPostForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         form = BlogPostForm()
#     context = {'title':'Contact','form': form}
#     return render(request, 'form.html',context)