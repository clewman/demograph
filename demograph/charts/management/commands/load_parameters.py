
from django.core.management.base import BaseCommand

import pandas as pd
from charts.models import Data_Parameter


class Command(BaseCommand):

    def handle(self, *args, **options):

        if params not in Data_Parameter.objects.get(params=params):
            params = {"counter": "0"}

            params.save()