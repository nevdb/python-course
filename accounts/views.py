from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer


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
            login(request, user)
            return redirect('login')
            # return HttpResponse('You have been registered successfully')
            # return HttpResponseRedirect('login')

    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registerForm})

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/profile_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles': queryset})
    
class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/profile.html'

    def get(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile, data=request.data)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')    