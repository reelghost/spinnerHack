import requests

url = "https://xrpspin.com/api.php?act=login"

payload = "{\r\n  \"username\": \"victor67\",\r\n  \"password\": \"matako\"\r\n}"
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'loclang=en; login=1; loginauth=0f35daff9a036594c8a3c0c82e52be85; user=4729686324228037'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# # withdraw
import requests
import json

url = "https://xrpspin.com/api.php?act=withdrawXrp"

payload = json.dumps({
  "confirm": 0,
  "payout_value": 0.000025,
  "password": "Matako@1997",
  "xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV",
  "distTag": "322129133"
})
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'loclang=en; login=1; loginauth=f5fbef0178bb608e0d03eb35a76ab10e; user=5162666505451508'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
