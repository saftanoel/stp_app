import json
import requests
import random

from django.core.management.base import BaseCommand, CommandError
from statii.models import Statie


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cookies = {
            "JSESSIONID": "5F3F41E97A369B4E659985052E3DF015	",
            "ROUTEID": ".1"
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

        response = requests.get("https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS?isG"
                                "prsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode=&currentFilter=view"
                                "_routes&vehicleModelId=-1&startDate=24-02-2022+00:00:00&endDate=24-02-2022+23:59:59&sel"
                                "ectedRoutesForView=,7&selectPostionRoutesForView=&vehicleHistoryId=0", cookies=cookies)
        print(response.status_code)
        json_obj = response.json()

        for section in json_obj['Rute'][0]['Sections']:
            statie = section['startStation']
            Statie.objects.create(nume=statie["name"], StatieID=statie["id"], long=statie['lon'], lat=statie['lat'])

