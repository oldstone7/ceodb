from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput




class CreateUserForm(UserCreationForm):


    username = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    password1 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 100%;'}),required=False)
    password2 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 100%;'}),required=False)
    email = forms.EmailField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    first_name = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    last_name = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    phone = forms.IntegerField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    street = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),max_length=30,required=False)
    city = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),max_length=30,required=False)
    state = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),max_length=30,required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 
                 'street', 'city', 'state']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.fields['username'].widget.attrs.update({
                'type':"username",
                'id':"username",
                'name':"username",
                'placeholder':"Enter your username"                      
            })
        self.fields['password1'].widget.attrs.update({
                'type':"password",               
                'id':"password1",
                'name':"password1",
                'placeholder':"Enter your password"                      
            })
        self.fields['password2'].widget.attrs.update({
                'type':"password",               
                'id':"password2",
                'name':"password2",
                'placeholder':"Repeat Password"                      
            })
        self.fields['email'].widget.attrs.update({
                'type':"email",               
                'id':"email",
                'name':"email",
                'placeholder':"Enter your email"                      
            })
        self.fields['first_name'].widget.attrs.update({
                'type':"text",               
                'id':"first_name",
                'name':"first_name",
                'placeholder':"Enter your First name"                      
            })
        self.fields['last_name'].widget.attrs.update({
                'type':"text",               
                'id':"last_name",
                'name':"last_name",
                'placeholder':"Enter your Last name"                      
            })
        self.fields['phone'].widget.attrs.update({
                'type':"number",               
                'id':"phone",
                'name':"phone",
                'placeholder':"Enter your phone number"                      
            })
        self.fields['city'].widget.attrs.update({
                'type':"text",               
                'id':"city",
                'name':"city",
                'placeholder':"Enter your city"                      
            })
        self.fields['street'].widget.attrs.update({
                'type':"text",               
                'id':"street",
                'name':"street",
                'placeholder':"Enter door no. and street"                      
            })
        self.fields['state'].widget.attrs.update({
                'type':"text",               
                'id':"state",
                'name':"state",
                'placeholder':"Enter your state"                      
            })
        





class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
        password = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 100%;'}),required=False)
        

        def __init__(self, *args, **kwargs):           
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs.update({
                'type':"username",
                
                'id':"username",
                'name':"username",
                'placeholder':"Enter your username"                      
            })

            self.fields['password'].widget.attrs.update({
                'type':"password",
                
                'id':"password",
                'name':"password",
                'placeholder':"Enter your password"                      
            })










