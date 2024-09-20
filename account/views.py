from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .forms import RegisterUser, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import Profile, User
from django.contrib.auth.decorators import login_required
from trip.models import Trip


def dashboard(request):
    trips = Trip.objects.filter(user=request.user)
    # If using the Profile model
    profile = Profile.objects.get(user=request.user)

    # If only using the User model
    user = request.user
    # Pass both the user and profile info (if applicable) to the template
    context = {
        'user': user,
        'profile': profile,
        'trips':trips,
    }
    return render(request, 'account/dashboard.html', context)

# register


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            Profile.objects.create(user=var)
            messages.success(
                request, 'Your account have been created succefully')
            return redirect('login')

        else:
            messages.warning(request, "something went wrong")
            return redirect('register')

    else:
        form = RegisterUser(request.POST)
        context = {'form': form}
        return render(request, 'account/register.html', context)

# update profile


def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            user.has_profile = True
            var.save()
            user.save()
            messages.info(
                request, 'Your profile details,has been updated successfuly')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'account/update_profile.html', context)


# view profile details
def profile_details(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    user = profile.user  # Assuming Profile has a OneToOne relationship with User
    context = {
        'profile': profile,
        'user': user
    }

    return render(request, 'account/profile_details.html', context)

# login


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "something went wrong")
            return redirect('login')

    return render(request, 'account/login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('login')


# Edit profile
