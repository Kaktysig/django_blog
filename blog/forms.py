from blog.models import Articles, Comments
from django import forms

class NewArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('name', 'content', 'comments_on',)


class NewComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', )


class EditArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('name', 'content',)