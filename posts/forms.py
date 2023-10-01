from django import forms

class CreatePostForm(forms.Form):
    preview = forms.FileField(required=False)
    title = forms.CharField(min_length=3, max_length=32)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(min_value=1, max_value=5)