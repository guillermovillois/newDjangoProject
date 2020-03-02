from django import forms
from .models import BlogPost
from django.forms import ModelForm

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','slug','content']


    def clean_title(self, *args, **kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        print(title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('This has already been used.')
        return title