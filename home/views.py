from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request, mk1, mk2):
    dict = {
        "name":"Jubayer",
        "ID":20201040,
        "courses":["CSE 309", "CSE 310", "CSE 303", "CSE 304"],
        "mark": int(mk1),
        "mark2":int(mk2)
    }

    return render(request, "home/home.html", context = dict)
