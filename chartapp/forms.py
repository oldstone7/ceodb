from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Operations
from django.contrib.auth.forms import SetPasswordForm




class CustomSetPasswordForm(SetPasswordForm):

    password1 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 80%;'}),required=False)
    password2 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 80%;'}),required=False)



    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

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
        




class OperationsForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = ['inventory', 'nos1', 'nos2']
        widgets = {
            'inventory': forms.TextInput(attrs={'required': False}),
            'nos1': forms.NumberInput(attrs={'required': False}),
            'nos2': forms.NumberInput(attrs={'required': False}),
        }        




class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               'id': 'firstName',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              'id': 'lastName',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             'id': 'username',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           'id': 'email',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'repeatPassword',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']




'''
class CreateUserForm(UserCreationForm):


    username = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    password1 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 81%;'}),required=False)
    password2 = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 81%;'}),required=False)
    email = forms.EmailField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    first_name = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    last_name = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    phone = forms.IntegerField(widget=TextInput(attrs={'style': 'width: 100%;'}),required=False)
    street = forms.CharField(widget=TextInput(attrs={'style': 'width: 100%;'}),max_length=30,required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 
                 'street']



    
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
        self.fields['street'].widget.attrs.update({
                'type':"text",               
                'id':"street",
                'name':"street",
                'placeholder':"Enter door no. and street"                      
            })
    
'''



class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput(attrs={'style': 'width: 95%;'}),required=False)
        password = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 77%;'}),required=False)
        

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










