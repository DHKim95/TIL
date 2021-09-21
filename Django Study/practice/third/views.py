from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    restaurant = Restaurant.objects.all()
    paginator = Paginator(restaurant, 5)

    page = request.GET.get('page') ## third/list?page=1
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)