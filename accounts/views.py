from django.views.generic import CreateView
# from accounts.models import Profile
from django.contrib.auth.models import User


class ProfileView(CreateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'accounts/templates/profile/profile_form.html'
