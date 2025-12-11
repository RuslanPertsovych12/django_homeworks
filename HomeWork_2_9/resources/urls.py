from django.urls import path
from . import views

urlpatterns = [
    path("", views.resources_list, name="resources-list"),
    path("<int:pk>/", views.resource_detail, name="resource-detail"),
    path("<int:pk>/send/", views.send_email_view, name="send-email"),
    path("register/", views.register_view, name="register"),
]
