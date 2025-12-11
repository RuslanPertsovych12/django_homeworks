from django.core.mail import send_mail
from django.conf import settings

def send_resource_email(to_email, resource):
    url = f"https://yourdomain.com/resources/{resource.id}/"

    send_mail(
        "Ваш ресурс",
        f"Ось посилання: {url}",
        settings.EMAIL_HOST_USER,
        [to_email],
    )
