from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import User


def index(request):
    users = User.objects.order_by('id')
    context = {'users': users}
    return render(request, 'users/index.html', context)


def detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'users/detail.html', {'user': user})
