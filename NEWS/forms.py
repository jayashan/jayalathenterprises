from django import forms
from .models import *



class NewsForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title', 'title_tag', 'author', 'image', 'category', 'body')

        widgets={
                    'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert the title Name'}),
                    'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                    'author':forms.Select (attrs={'class':'form-control'}),
                    'category':forms.Select (attrs={'class':'form-control'}),
                    'body':forms.Textarea(attrs={'class':'form-control'}),
                }


class EditNewsForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title', 'title_tag', 'author', 'image', 'category', 'body')

        widgets={
                    'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert the title Name'}),
                    'title_tag':forms.TextInput(attrs={'class':'form-control'}),
                    'author':forms.Select (attrs={'class':'form-control'}),
                    'category':forms.Select (attrs={'class':'form-control'}),
                    'body':forms.Textarea(attrs={'class':'form-control'}),
                }