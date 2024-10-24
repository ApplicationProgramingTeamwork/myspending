from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    # 你可以添加其他字段，例如 remember me
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # 可以在这里添加自定义验证逻辑
        return cleaned_data
