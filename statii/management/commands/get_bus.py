import json
import requests
import random
import time
from django.core.management.base import BaseCommand, CommandError
from statii.models import Statie, Autobuz

from django_cron import CronJobBase, Schedule


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
            cookies = {
                "JSESSIONID": "59A5517CF1F113F732E5529CFC10A971",
                "ROUTEID": ".2"
            }

            url = "https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS?isGprsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode=&currentFilter=view_current_positions&vehicleModelId=-1&startDate=22-06-2022+00%3A00%3A00&endDate=22-06-2022+23%3A59%3A59&selectedRoutesForView=&selectPostionRoutesForView=7&vehicleHistoryId=0"

            while True:
                response = requests.get(url, cookies=cookies)
                print(response.status_code)
                json_obj = response.json()

                # print(response.json())

                for element in json_obj["Vehicles"]:
                    autobuz = element["Latitudine"]
                    Autobuz.objects.create(nrInm=element["NrInmat"], idBus=element["IdVehicul"],
                                           long=element["Longitudine"],
                                           lat=element["Latitudine"])
                # print(element["Latitudine"])
                # print(" ")
                # print(element["Longitudine"])
                # print(" ")
                # print(element["IdVehicul"])
                # print(" ")
                # print(element["NrInmat"])
                print(autobuz)
                time.sleep(10)





