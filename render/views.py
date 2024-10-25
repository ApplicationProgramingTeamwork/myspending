from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipt, Product
from django.contrib.auth.decorators import login_required
from .forms import ReceiptForm, ProductForm


@login_required
def home(request):
    receipts = Receipt.objects.filter(
        owner=request.user).order_by('date_added')
    context = {'receipts': receipts}
    return render(request, 'render/home.html', context)


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(
        owner=request.user).order_by('date_added')
    context = {'receipts': receipts}
    return render(request, 'render/receipt.html', context)


@login_required
def receipt_detail(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id, owner=request.user)
    products = Product.objects.filter(receipt=receipt)
    context = {'receipt': receipt, 'products': products}
    return render(request, 'render/receipt_detail.html', context)


@login_required
def product_list(request):
    products = Product.objects.order_by('date_added')
    context = {'products': products}
    return render(request, 'render/product.html', context)


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'render/product_detail.html', context)


@login_required
def new_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(data=request.POST)
        if form.is_valid():
            new_receipt_form = form.save(commit=False)
            new_receipt_form.owner = request.user
            new_receipt_form.save()
            return redirect('render:receipts')
    else:
        form = ReceiptForm()

    context = {'form': form}
    return render(request, 'render/new_receipt.html', context)


@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('render:products')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'render/new_product.html', context)


@login_required
def edit_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, owner=request.user)

    if request.method != 'POST':
        form = ReceiptForm(instance=receipt)
    else:
        form = ReceiptForm(instance=receipt, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('render:receipt_detail', receipt_id=receipt.id)

    context = {'form': form, 'receipt': receipt}
    return render(request, 'render/edit_receipt.html', context)


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('render:product_detail', product_id=product.id)

    context = {'form': form, 'product': product}
    return render(request, 'render/edit_product.html', context)
