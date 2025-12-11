from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core.paginator import Paginator

from .models import Resource
from .forms import RegisterForm
from .emails import send_resource_email

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("resources-list")
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})


def resources_list(request):
    resources = Resource.objects.all()
    paginator = Paginator(resources, 5)
    page = request.GET.get("page")
    items = paginator.get_page(page)
    return render(request, "resources_list.html", {"items": items})


def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, "resource_detail.html", {"resource": resource})


def send_email_view(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    send_resource_email(request.user.email, resource)
    return redirect("resource-detail", pk=pk)