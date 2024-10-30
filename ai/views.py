from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from ai.forms import PhotoUploadForm
from ai.gemini import send_photo_to_gemini
from django.contrib.auth.decorators import login_required
from render.forms import ProductForm, ReceiptForm
from dateutil import parser
import json


@login_required
def upload_photo(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid request method. Please use POST.")

    form = PhotoUploadForm(request.POST, request.FILES)
    if form.is_valid() == False:
        return HttpResponseBadRequest("Invalid form data. Please check the form and try again.")

    try:
        photo = form.cleaned_data['photo']
        json_string = send_photo_to_gemini(photo.temporary_file_path())
        data = json.loads(json_string)
        receipt_form = ReceiptForm({
            'storeName': data.get('storeName'),
            'storeAddress': data.get('storeAddress'),
            'totalPrice': data.get('totalPrice'),
            'date': parser.parse(data.get('date')),
        })

        if receipt_form.is_valid() == False:
            print(data)
            print(receipt_form.errors)

        receipt = receipt_form.save(commit=False)
        receipt.owner = request.user
        receipt.set_picture(photo)
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
            if product_form.is_valid() == False:
                print(item)
                print(product_form.errors)
            product_form.save()

        return HttpResponseRedirect(reverse('render:receipt_detail', args=[receipt.id]))

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"JSON string: {json_string}")
        return HttpResponseRedirect(f'{reverse("render:home")}?error=Oops! The receipt recognition failed. Please check the quality of the image and re-upload.')
