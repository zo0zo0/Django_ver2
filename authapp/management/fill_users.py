from django.core.management.base import BaseCommand
from mimesis import Person
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_count = 10

        ShopUser.objects.all().delete()
        for _ in range(user_count):
            person = Person('en')
            new_user = ShopUser(username=person.username(),
                                password=person.password(),
                                first_name=person.name(),
                                last_name=person.last_name(),
                                age=person.age(),
                                email=person.email(domains=['example.com']),
                                avatar=person.avatar()
                                )
            new_user.save()

        super_user = ShopUser.objects.create_superuser('django', '', 'geekbrains', age=43)