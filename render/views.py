import json
from django.shortcuts import render


def home(request):
    jsonString = request.GET.get('json', '')
    if jsonString:
        data = json.loads(jsonString)
    else:
        data = None
    return render(request, 'render/home.html', {'data': data})
