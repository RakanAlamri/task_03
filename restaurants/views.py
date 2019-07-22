from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [
            {
                "restaurant_name":"McDonald's",
                "food_type":"American",
            },
            {
                "restaurant_name":"Piato",
                "food_type":"italian",
            },
            {
                "restaurant_name":"Tokyo",
                "food_type":"Japaneese",
            },
        ],


    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
            "restaurant_name":"Tokyo",
            "food_type":"Japaneese",
            
        },

    }
    return render(request, 'detail.html', context)
