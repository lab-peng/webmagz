from django import forms
from .models import Comment
from mptt.forms import TreeNodeChoiceField


class CommentCreateForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('parent', 'content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }