import json
import requests
import random

from django.core.management.base import BaseCommand, CommandError
from statii.models import Statie, Autobuz


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 3 seconds
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'buses.my_cron_job'    # a unique code

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cookies = {
            "JSESSIONID": "C05643178B2C7E0B2CC920AE3000E273",
            "ROUTEID": ".1"
        }

        response = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS?isGprsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode=&currentFilter=view_current_positions&vehicleModelId=-1&startDate=22-06-2022+00%3A00%3A00&endDate=22-06-2022+23%3A59%3A59&selectedRoutesForView=&selectPostionRoutesForView=7&vehicleHistoryId=0", cookies=cookies)
        print(response.status_code)
        json_obj = response.json()

        #print(response.json())

        for element in json_obj["Vehicles"]:
            autobuz = element["Latitudine"]
            Autobuz.objects.create(nrInm=element["NrInmat"], idBus=element["IdVehicul"], long=element["Longitudine"], lat=element["Latitudine"])
            #print(element["Latitudine"])
            #print(" ")
            #print(element["Longitudine"])
            #print(" ")
            #print(element["IdVehicul"])
            #print(" ")
            #print(element["NrInmat"])
