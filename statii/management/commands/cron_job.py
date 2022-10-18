from django_cron import CronJobBase, Schedule
import requests
from statii.models import Statie, Autobuz

class CronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'    # a unique code

    def do(self):
        cookies = {
            "JSESSIONID": "75E57FEB95FDE2F116EB0F79A3B49817",
            "ROUTEID": ".1"
        }

        response = requests.get(
            "https://avl-albaiulia.radcom.ro/avl-ab/monitor/vehicleVectorialMap/getVehiclesGPRS?isGprsConnected=-1&inTime=-1&vehicleTypeId=-1&vehicleId=-1&vehicleCode=&currentFilter=view_current_positions&vehicleModelId=-1&startDate=22-06-2022+00%3A00%3A00&endDate=22-06-2022+23%3A59%3A59&selectedRoutesForView=&selectPostionRoutesForView=7&vehicleHistoryId=0",
            cookies=cookies)
        print(response.status_code)
        json_obj = response.json()

        # print(response.json())

        for element in json_obj["Vehicles"]:
            autobuz = element["Latitudine"]
            Autobuz.objects.create(nrInm=element["NrInmat"], idBus=element["IdVehicul"], long=element["Longitudine"],
                                   lat=element["Latitudine"])
            # print(element["Latitudine"])
            # print(" ")
            # print(element["Longitudine"])
            # print(" ")
            # print(element["IdVehicul"])
            # print(" ")
            # print(element["NrInmat"])
