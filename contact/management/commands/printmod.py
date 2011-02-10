from django.core.management.base import AppCommand
from django.db import models


class Command(AppCommand):
    help = "Prints the models in app, and count objects for each"

    def handle_app(self, app, **options):
        app_models = models.get_models(app)
        self.stdout.write("Models in: " + app.__name__)
        self.stdout.write('\n')
        for item_model in models.get_models(app):
            name = item_model._meta.object_name
            count = str(item_model.objects.all().count())
            self.stdout.write(name + " " + count + '\n')                      
            self.stderr.write("Error: " + name + " " + count + '\n') 
