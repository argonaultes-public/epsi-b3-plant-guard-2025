from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Plant
from django.core.serializers.json import DjangoJSONEncoder


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
    return render(
        req,
        'plants.html'
    )

def plants_json(req):
    plants = Plant.objects.values()
    return JsonResponse(
        list(plants),
        safe=False)