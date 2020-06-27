from django import forms
from accounts.models import AuthUser

class LoginForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields = "__all__"
