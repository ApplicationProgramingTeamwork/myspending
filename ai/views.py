from django.http import HttpResponseRedirect
from django.urls import reverse

from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini

from django.core.files.uploadedfile import InMemoryUploadedFile


def handle_uploaded_file(file):
    if isinstance(file, InMemoryUploadedFile):
        file_content = file.read()
        print("File content length:", len(file_content))
    else:
        temp_path = file.temporary_file_path()
        print("Temporary file path:", temp_path)


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            try:
                file = photo.temporary_file_path()  # 如果是大文件
            except AttributeError:
                file = photo.read()
            json = send_photo_to_gemini(file)
            url = reverse('home')
            return HttpResponseRedirect(f'{url}?json={json}')
