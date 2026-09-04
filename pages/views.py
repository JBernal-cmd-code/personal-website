from django.shortcuts import render

def home(request):
    goals = [
        {"name": "Maintain an A or B in all my classes", "completed": True},
        {"name": "Collect my dream Choso figure", "completed": False},
        {"name": "Get a new car by the end of the year", "completed": False},
        {"name": "Get a new monitor for my computer", "completed": True},
        {"name": "Become a better cooker", "completed": False},
    ]
    return render(request, "home.html", {"goals": goals})

def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
