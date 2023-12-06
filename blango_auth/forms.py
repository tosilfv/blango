from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm

from blango_auth.models import User


class BlangoRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(BlangoRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))

# from datetime import timedelta

# from django.conf import settings
# from django.utils import timezone

# from blango_auth.models import User
# User.objects.filter(
#     is_active=False,
#     date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
# ).delete()