from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import ResetPasswordForm
from django import forms
from django.contrib.auth.models import User

# Custom user creation form


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

# Custom user change form


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

# Custom password reset form for allauth


class MyCustomResetPasswordForm(ResetPasswordForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "There is no user registered with this email address.")
        return email

    def save(self, request):
        # Call the parent class's save method
        email_address = super(MyCustomResetPasswordForm, self).save(request)

        # Add any additional processing logic here
        if self.users:
            user_emails = ', '.join([user.email for user in self.users])
            print(f"Password reset requested for: {user_emails}")

        # Return the original result
        return email_address
