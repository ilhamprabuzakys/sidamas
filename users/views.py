from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UpdateUserForm, UpdateProfileForm
from django.shortcuts import redirect, render
from . import models

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)
    
class UsersBaseView(GlobalPermissionMixin, LoginRequiredMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RegistrasiUserList(UsersBaseView,View):
    template_name = "registrasi/list_users.html"
    
    def get(self, request):
        return render(request, self.template_name)

class UserVerificationListView(UsersBaseView, View):
    template_name = "verified/list_users.html"
    
    def get(self, request):
        user = request.user
        role = user.profile.role

        list_profile_users = models.Profile.objects.filter(is_verified=False)

        if role == "psm":
            list_profile_users = list_profile_users.filter(role="psm")
        elif role == "dayatif":
            list_profile_users = list_profile_users.filter(role="dayatif")

        context = {"list_profile_users": list_profile_users}
        return render(request, self.template_name, context)

class MyProfile(LoginRequiredMixin,View):
    
    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'profile.html', context)
    
    def post(self,request):
        user_form = UpdateUserForm(
            request.POST,
            instance=request.user
        )
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('dashboard:profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'users/profile.html', context)
    