from django.http import HttpResponseRedirect
from django.urls import reverse

from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            json = send_photo_to_gemini(photo.temporary_file_path())
            url = reverse('home')
            return HttpResponseRedirect(f'{url}?json={json}')
