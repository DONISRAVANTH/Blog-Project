from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser  # Corrected typo here
        fields = ['username', 'email', 'fullname', 'password1', 'password2']
        