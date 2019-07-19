from django.shortcuts import render
from .models import Restaurant, Category

# Create your views here.

def index(request) :
    return render(request, 'index.html')

def convin(request) :
    return render(request, 'convin.html')

def map(request) :
    return render(request, 'map.html')

def hotplace(request) :
    restaurant = Restaurant.objects
    check = '1'
    category = '한식'
    f_c = request.GET.get('food_category')
    if f_c == 'korean' :
        check = 1
        category = '한식'
    elif f_c == 'chinese' :
        check = 2
        category = '중식'
    elif f_c == 'japanese' :
        check = 3
        category = '일식'
    elif f_c == 'western' :
        check = 4
        category = '양식'
    elif f_c == 'snack' :
        check = 5
        category = '분식'
    food_filter = Restaurant.objects.filter(cate = check)

    locate = '정문'
    l_c = request.GET.get('location_category')
    if l_c == 'main':
        locate = '정문'
    elif l_c == 'side':
        locate = '쪽문'
    elif l_c == 'rotary':
        locate = '로타리'
    location_filter = Restaurant.objects.filter(locate = locate)

    return render(request, 'hotplace.html',
    {'restaurant':restaurant, 'food' : food_filter,'location' : location_filter,
    'f_category': category, 'l_category' : locate})