import requests
import json
from time import sleep


def login(url_login, payload):
  response_login = session.post(url_login, json=payload)
  response_data = json.loads(response_login.text)
  if response_login.status_code == 200: # if request made successfully
      print(response_data['parameters'][-1])

def withdraw(url_withdraw, payload):
  response_withdraw = session.post(url_withdraw, json=payload)
  print(response_withdraw.status_code)
  # response_data = json.loads(response_withdraw.text)
  if response_withdraw.status_code == 200:
      print(response_withdraw.text)

# Create a session object to persist the session data
session = requests.Session()
# urls constants
url_login = "https://xrpspin.com/api.php?act=login"
url_withdraw = "https://xrpspin.com/api.php?act=withdrawXrp"


# payloads constants
payload_logins = [
  {"username": "ghoster","password": "Matako@1997"},
  {"username": "masikio","password": "Matako"},
  {"username": "fatuu5","password": "matako"},
  {"username": "jeflet","password": "matako"},
  {"username": "pacha5","password": "matako"},
]
payload_withdraws = [
  {"confirm": 0, "payout_value": 0.000025,"password": "Matako@1997","xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV","distTag": "322129133"},
  {"confirm": 0, "payout_value": 0.000025,"password": "Matako","xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV","distTag": "322150283"},
  {"confirm": 0, "payout_value": 0.000025,"password": "matako","xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV","distTag": "322386002"},
  {"confirm": 0, "payout_value": 0.000025,"password": "matako","xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV","distTag": "322400834"},
  {"confirm": 0, "payout_value": 0.000025,"password": "matako","xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV","distTag": "322701029"},
  ]


# a for loop for all accounts
z = 1
while True:
  print(z)
  for i in range(len(payload_logins)):
    login(url_login, payload_logins[i])
    withdraw(url_withdraw, payload_withdraws[i])
  sleep(60)
  z += 1
  


