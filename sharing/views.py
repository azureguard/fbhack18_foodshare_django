from django.shortcuts import render, redirect, get_object_or_404
from sharing.forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import User, Profile


# Create your views here.

def user_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = get_object_or_404(Profile, pk=user_id)
    return render(request, 'sharing/user_details.html',
                  {'user': user, "profile": profile})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'sharing/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def index(request):
    return render(request, 'sharing/home.html')

def group_buy(request):
    return render(request, 'sharing/group_buy.html')

def sharing(request):
    return render(request, 'sharing/index.html')