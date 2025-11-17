from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def hello(request, name, year):
    return HttpResponse(f"<h1>Hello {name}! Тобі {year} років.</h1>")

def hello2(request):
    name = request.GET.get("name", "Гість")
    year = request.GET.get("year", None)

    try:
        year = int(year)
    except (TypeError, ValueError):
        year = None

    if year:
        current_year = datetime.now().year
        age = current_year - year
    else:
        age = "невідомий"

    return HttpResponse(f"Hello {name}! Твій вік: {age}.")

@csrf_exempt
def hello3(request):
    if request.method != "POST":
        return HttpResponse("Будь ласка, використовуйте POST-запит.")

    name = request.POST.get("name", "Гість")
    year = request.POST.get("year")

    # Якщо рік некоректний — None
    try:
        year = int(year)
    except (TypeError, ValueError):
        year = None

    if year:
        current_year = datetime.now().year
        age = current_year - year
    else:
        age = "невідомий"

    return HttpResponse(f"Hello {name}! Твій вік: {age}.")


def compress(text: str) -> str:
    if not text:
        return ""

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            char = text[i - 1]
            if char == " ":
                char = "_"
            result.append(f"{char}{count}")
            count = 1

    last_char = text[-1]
    if last_char == " ":
        last_char = "_"
    result.append(f"{last_char}{count}")

    return "".join(result)


def decompress(text: str) -> str:
    result = []
    i = 0

    while i < len(text):
        char = text[i]
        i += 1

        num = ""
        while i < len(text) and text[i].isdigit():
            num += text[i]
            i += 1

        if char == "_":
            char = " "
        result.append(char * int(num))

    return "".join(result)


@csrf_exempt
def comp_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "")
        compressed = compress(text)
        return JsonResponse({"compressed": compressed})
    return JsonResponse({"error": "POST required"}, status=405)


@csrf_exempt
def decomp_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "")
        decompressed = decompress(text)
        return JsonResponse({"decompressed": decompressed})
    return JsonResponse({"error": "POST required"}, status=405)