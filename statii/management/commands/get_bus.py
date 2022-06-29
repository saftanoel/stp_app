import json
import requests
import random

from django.core.management.base import BaseCommand, CommandError
from statii.models import Statie


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cookies = {
            "JSESSIONID": "E22F7BB1E2F4B548EC79101463098990",
            "ROUTEID": ".2"
        }

      #   response = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleLinearMap/getPanels",
      #                           cookies=cookies)
      #
      #   json_obj = response.json()
      #
      #   for station in json_obj['Routes'][0]['RouteStations']:
      #      # print(id_statie)
      #      # print(station["StationName"])
      #       #Statie.objects.create(nume=station["StationName"], StatieID=station["StationId"], long=0, lat=0)

        response = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS?isGprsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode=&currentFilter=view_current_positions&vehicleModelId=-1&startDate=22-06-2022+00%3A00%3A00&endDate=22-06-2022+23%3A59%3A59&selectedRoutesForView=&selectPostionRoutesForView=7&vehicleHistoryId=0", cookies=cookies)
        print(response.status_code)
        json_obj = response.json()

        #print(response.json())

        for element in json_obj["Vehicles"]:
            autobuz = element["Latitudine"]
            print(autobuz)
            print(" ")
            print(element["Longitudine"])
