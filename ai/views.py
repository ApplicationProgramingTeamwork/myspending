from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini
import json


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            jsonString = send_photo_to_gemini(photo.temporary_file_path())
            url = reverse('ai:upload_photo')
            return HttpResponseRedirect(f'{url}?json={jsonString}')

    languages = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')
    jsonString = request.GET.get('json', '')
    if jsonString:
        data = json.loads(jsonString)
    else:
        data = None
    return render(request, 'ai/index.html', {'data': data, 'language': languages[0]})
