from django.core.management.base import BaseCommand
from django.db import models
from django.conf import settings
from django.utils.importlib import import_module


class Command(BaseCommand):
    help = "Prints the models in app, and count objects for each"

    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            app = import_module(app + '.models')
            app_models = models.get_models(app)
            self.stdout.write("Models in: " + app.__name__)
            self.stdout.write('\n')
            for item_model in app_models:
                name = item_model._meta.object_name
                count = str(item_model.objects.all().count())
                self.stdout.write(name + " " + count + '\n')
                self.stderr.write("Error: " + name + " " + count + '\n')
