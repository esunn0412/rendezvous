from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'text-start editable',
                                                           'style': 'height:auto'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'content', 'project']