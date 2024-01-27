from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic

def register(request):
    if request.method == 'POST': 
        register_form = forms.RegistrationForm(request.POST) 
        if register_form.is_valid(): 
            register_form.save() 
            return redirect('login') 
    else: 
        register_form = forms.RegistrationForm() 
        return render(request, 'register.html',{'form':register_form,'type':'Registration'})

    
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    
class LogOut(generic.View):
    def get(self, request):
        logout(request)
        return redirect('home')