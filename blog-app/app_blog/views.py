from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(
        request,
        "app_blog/home.html",
        {"title": "Главная страница"}
    )