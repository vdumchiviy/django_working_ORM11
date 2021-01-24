from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort in ('name', 'price', '-price'):
        phones = Phone.objects.order_by(sort)
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(f"slug = {slug}")
    phone = Phone.objects.filter(slug=slug).get()
    context = {'phone': phone}
    # a = 1/0
    return render(request, template, context)
