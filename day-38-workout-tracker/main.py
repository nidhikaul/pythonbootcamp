import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 200
AGE = 40

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
prompt = input("Tell me which exercises you did:")
user_params = {
 "query": prompt,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

headers_prompt = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": TOKEN
}

response = requests.post(url=exercise_endpoint,json=user_params, headers=headers_prompt)
result = response.json()

sheety_endpoint = SHEET_ENDPOINT

headers = {
    "Content-Type": "application/json"
}


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint,json=sheet_inputs,headers=headers_prompt)
print(sheet_response.text)