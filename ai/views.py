from django.http import HttpResponseRedirect
from django.urls import reverse
from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini
from django.contrib.auth.decorators import login_required
from render.forms import ProductForm, ReceiptForm
from dateutil import parser
import json


@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            json_string = send_photo_to_gemini(photo.temporary_file_path())
            data = json.loads(json_string)
            receipt_form = ReceiptForm({
                'storeName': data.get('storeName'),
                'storeAddress': data.get('storeAddress'),
                'totalPrice': data.get('totalPrice'),
                'date': parser.parse(data.get('date')),
            })
            if receipt_form.is_valid():
                receipt = receipt_form.save(commit=False)
                receipt.owner = request.user
                receipt.save()

                for item in data['items']:
                    product_data = {
                        'receipt': receipt,
                        'name': item.get('name'),
                        'nameEnglish': item.get('nameEnglish'),
                        'nameChinese': item.get('nameChinese'),
                        'price': item.get('price'),
                        'discount': item.get('discount')
                    }
                    product_form = ProductForm(product_data)
                    if product_form.is_valid():
                        product_form.save()
                    else:
                        print(item)
                        print(product_form.errors)
                return HttpResponseRedirect(reverse('render:receipt_detail', args=[receipt.id]))
            else:
                print(data)
                print(receipt_form.errors)

    return HttpResponseRedirect(reverse('render:home'))
