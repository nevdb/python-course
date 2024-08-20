from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text", "comment_author_name", "comment_author_email", "comment_published_date")
        widgets = {
            "comment_author_name":forms.TextInput(attrs={"class":"col-sm-12"}),
            "comment_author_email":forms.TextInput(attrs={"class":"col-sm-12"}),
            "comment_text":forms.Textarea(attrs={"class":"form-control"})

        }

