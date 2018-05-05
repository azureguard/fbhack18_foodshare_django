from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def UserLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # user = authenticate(request, username=username, password=password)
    if user is not None:
        # login(request, user)
        pass
        # Redirect to a success page.

    else:
        # Return an 'invalid login' error message.
        return ("Invalid login. Please try again.")


def UserLogout(request):
    logout(request)
    # Redirect to a success page.