from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Author

# Create your views here.

def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"
    
    def get_context_data(self):
        car_list = Car.objects.all()
        return {
            "car_list": car_list
        }


def my_view_car(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"}
    ]
    
    car_list_2 = Car.objects.all()
    
    context = {
        "car_list_2": car_list_2
    }
    return render(request, "my_first_app/car_list.html", context)


#crea una vista de los autores
def my_view_authors(request):
    #se trae todos los valores de author de la BD
    authors_list = Author.objects.all()
    
    context = {
        "authors_list": authors_list
    }

    return render(request, "my_first_app/author_list.html", context)

