import requests
import os
from datetime import datetime
from dotenv import load_dotenv
# from pathlib import Path

load_dotenv()
USER = os.environ.get('USER')
TOKEN = os.environ.get('TOKEN')
GRAPHID = os.environ.get('GRAPHID')
pixela_endpoint = "https://pixe.la/v1/users"
DUMMY = os.environ.get('DUMMY')

user_params = {
    "token": TOKEN,
    "user": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

###Create user - POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

###Create Graph - POST
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

# graph_config = {
#     "id": GRAPHID,
#     "name": "Upskill Graph",
#     "unit": "days",
#     "type": "int",
#     "color": "kuro"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

###Create a pixel - POST

pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}"
# today = datetime.now()
# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=pixel_endpoint,json=pixel_config, headers=headers)
# print(response.text)

##Updating the existing data - PUT

# today = datetime(year=2022, month=12, day=21)
today = datetime.now()

update_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "10"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.put(url=update_endpoint,json=update_config, headers=headers)
print(response.text)

###Deleting a pixel - DEL
# today = datetime(year=2022, month=12, day=14)
# del_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.delete(url=del_endpoint,headers=headers)
# print(response.text)


