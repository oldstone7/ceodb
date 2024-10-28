from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Finance
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import TextInput, PasswordInput
from .models import Product


class UserForm(forms.ModelForm):

    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}),
        }





class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'num_of_products']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category'}),
            'num_of_products': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Products'}),
        }




class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['Client', 'order', 'cash', 'amount', 'liquid', 'asset', 'liab', 'date']
        widgets = {
            'Client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Client Name'}),
            'order': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Order Name'}),
            'cash': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cash'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'liquid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Liquidity Value'}),
            'asset': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Asset Value'}),
            'liab': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Liabilities Value'}),
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }



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






class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=TextInput(attrs={'style': 'width: 100%;'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'style': 'width: 100%;'}), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'type': "email",
            'id': "email",
            'name': "email",
            'placeholder': "Email",
            'class': "form-control"
        })

        self.fields['password'].widget.attrs.update({
            'type': "password",
            'id': "password",
            'name': "password",
            'placeholder': "Password",
            'class': "form-control"
        })









