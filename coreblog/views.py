from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

dict_months = {"Jeruary": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
               "August": 8, "September": 9, "October": 10,
               "November": 11, "December": 12}


def home(request):
    return HttpResponse("Hello World!")


def months_by_number(request, month):
    months = list(dict_months.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_month_path = reverse("month_str", args=[redirect_month])
    return HttpResponseRedirect(redirect_month_path)


def months(request, month):
    try:
        month_number = dict_months[month]
        return HttpResponse(f"<h1>{month_number}</h1>")
    except:
        return HttpResponseNotFound("Invalid Month")
