from django.views.generic import CreateView, UpdateView
from accounts.models import Profile
from accounts.forms import ProfileForm


class ProfileView(CreateView):
    model = Profile
    fields = ('name', 'email', 'job_title', 'bio')
    template_name = 'accounts/templates/profile/profile_form.html'


# class PersonUpdateView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'accounts/templates/profile/profile_update_form.html'
