from django import forms

from coreblog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            "user_name": "Your name",
            "email_field": "Your Email",
            "text_comment": "Your comment"
        }
