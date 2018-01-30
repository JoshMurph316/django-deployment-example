from django.forms import ModelForm
from app_two.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
