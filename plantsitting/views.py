from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Plant
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Plant):
            return str(obj)
        return super().default(obj)

# Create your views here.

def plants(req):
    plants = Plant.objects.all()
    return HttpResponse('<br>'.join(
        list(
            map(
                lambda plant: plant.name,
                plants
                )
            )
        )
    )

def plants_tpl(req):
    if req.user.is_authenticated:
        return render(
            req,
            'plants.html'
        )
    else:
        return redirect('login')

def plants_json(req):
    plants = Plant.objects.values()
    return JsonResponse(
        list(plants),
        safe=False)


def custom_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page or view
        return redirect('home')
    else:
        # Handle authentication failure
        return redirect('login')

def display_login(request):
    return render(request, 'login.html')