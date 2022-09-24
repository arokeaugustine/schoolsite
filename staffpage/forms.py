from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'password']



class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'type':"text",
            'class':"form-control w-100", 
            'id':"inputText",
           
        })
        self.fields["email"].widget.attrs.update({
            'type':"email",
            'class':"form-control",
            'id':"exampleInputEmail1", 
        })
        self.fields["content"].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'id':"message", 
        })
        

    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


