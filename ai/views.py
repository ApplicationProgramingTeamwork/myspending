from django.http import HttpResponseRedirect
from django.urls import reverse
from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini
from django.contrib.auth.decorators import login_required
import json

from render.forms import ProductForm, ReceiptForm


@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            json_string = send_photo_to_gemini(photo.temporary_file_path())
            data = json.loads(json_string)
            receipt_form = ReceiptForm(data)
            if receipt_form.is_valid():
                receipt = receipt_form.save(commit=False)
                receipt.owner = request.user
                receipt.save()

                for item in data['items']:
                    product_data = {
                        'receipt': receipt,
                        'name': item['name'],
                        'nameEnglish': item['nameEnglish'],
                        'nameChinese': item['nameChinese'],
                        'price': item['price'],
                        'discount': item['discount']
                    }
                    product_form = ProductForm(product_data)
                    if product_form.is_valid():
                        product_form.save()
                    else:
                        print(product_form.errors)
                return HttpResponseRedirect(reverse('render:receipt_detail', args=[receipt.id]))
            else:
                print(receipt_form.errors)

    return HttpResponseRedirect(reverse('render:home'))
