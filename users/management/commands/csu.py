from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email="admin@example.com",
            username="admin",
            phone_number="+7-900-000-00-00",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("admin")
        user.save()
