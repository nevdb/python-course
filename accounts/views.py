from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


@login_required
def profile(request):
    return render(request, 
                  'accounts/profile.html',
                  {'section': 'profile'})

def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            # The user will be active right after the registration, no need to confirm by email
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered successfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registerForm})
