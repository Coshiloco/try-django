from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'"{title}" already exists')
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "sarasa":
    #         raise forms.ValidationError('Que haces bobi?.')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "sarasa":
            self.add_error('title', 'No puedes tener un titulo igual a "Sarasa"')
        if "cósmica" in content:
            self.add_error('content', 'No puedes tener la palabra "cósmica" en el contenido')
        return cleaned_data