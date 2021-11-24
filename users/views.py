from django.db.models.signals import post_save
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! Login here')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', { 'form' : form })


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm()
        p_form = UpdateProfileForm()

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)