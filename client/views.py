from .models import ClubConsulting
from django.core.mail import send_mail
from .serializers import ClubConsultingSerializers
from rest_framework import generics
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests


class ClubConsultingView(generics.CreateAPIView):
    queryset = ClubConsulting.objects.all()
    serializer_class = ClubConsultingSerializers

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Получена новая заявка:\n"
        for key, value in data.items():
            if key in ["username", "phone_number"]:
                message_text += f"{key}: {value}\n"
        chat_id = "1880387683"
        bot_token = "5989553791:AAFQmZOoXgcW_XRPvuXatjUq5r1X7iSwr6E"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}
        requests.post(url, json=payload)

        return response


def send_contact(data):
    to_email = 'zhusupovaelmara80@gmail.com'
    send_mail(
        'Subject',
        f'{data}',
        'from@example.com',
        [to_email],
        fail_silently=False
    )


@receiver(post_save, sender=ClubConsulting)
def contact(instance, *args, **kwargs):
    send_contact(f"ФИО: {instance.username}\nНомер: {instance.phone_number}")
