from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    # 회원가입 폼
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_confirm_password(self):
        pw = self.cleaned_data
        if pw['password'] != pw['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')

        return pw['confirm_password']