from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Account


class Command(BaseCommand):
    help = _('Set up project functionality options and fill tables')

    @transaction.atomic()
    def handle(self, *args, **options):

        # create super user
        admin_email = 'root@spaceshop.com'
        admin_password = 'root'

        try:
            admin = Account.objects.get(email=admin_email)

            if admin:
                self.stdout.write(self.style.ERROR('Admin {} already exist'.format(admin_email)))

        except ObjectDoesNotExist:
            admin = Account(
                email=admin_email,
                is_staff=True,
                username='Administrator'
            )
            admin.set_password(admin_password)
            admin.save()

            self.stdout.write(self.style.SUCCESS(
                'Admin account created with email={} and password={}'.format(admin_email, admin_password)))
