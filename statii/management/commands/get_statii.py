import json
import requests
import random


from django.core.management.base import BaseCommand, CommandError
from statii.models import Statie


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cookies = {
            "JSESSIONID": "6C4B287590153048877F503720AF9696",
            "ROUTEID": ".1"
        }

        r = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleLinearMap/getPanels", cookies=cookies)
        print(r.status_code)

        json_obj = r.json()

        for element in json_obj['Routes']:
            for statie in element['RouteStations']:
                Statie.objects.create(nume=statie["StationName"], long=random.randint(0, 100), lat=random.randint(0,100))
                print(statie["StationName"])

    # def handle(self, *args, **options):
    #     cookies = {
    #         "JSESSIONID": "6C4B287590153048877F503720AF9696",
    #         "ROUTEID": ".1"
    #     }
    #
    #     response = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS"
    #                             "?isGprsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode"
    #                             "=&currentFilter=view_routes&vehicleModelId=-1&startDate=07-03-2022+00:00:00&endDate"
    #                             "=07-03-2022+23:59:59&selectedRoutesForView=,"
    #                             "7&selectPostionRoutesForView=&vehicleHistoryId=0", cookies=cookies)
    #     print(response.status_code)
    #
    #     json_obj2 = response.json()
    #
    #     for i in json_obj2['Rute']:
    #         for statie2 in i['startStation']:
    #             print(statie2["lat"], " ", statie2["lon"])
