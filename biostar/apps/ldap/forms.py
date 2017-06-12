from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label=("LDAP User"))
    password = forms.CharField(widget=forms.PasswordInput(), label=("Password"))
    remember = forms.BooleanField(label=("Remember Me"),
                                  required=False)

