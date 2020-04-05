from django.views.generic import CreateView
from accounts.models import Profile
# from django.contrib.auth.models import User


class ProfileView(CreateView):
    model = Profile
    fields = ('patronymic', 'birth_date')
    template_name = 'accounts/templates/profile/profile_form.html'
