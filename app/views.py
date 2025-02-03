from django.shortcuts import render, redirect
from .models import UserData
# Create your views here.
def home_page(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        if login and password:
            UserData.objects.create(login=login, password=password)  # Внимание: пароли лучше хешировать!
        return redirect("home_page")  # После успешной отправки перенаправляем пользователя
    return render(request, "index.html")

