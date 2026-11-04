import requests
import json
import csv
token_url = "https://capgemini-preprod.zslogin.net/oauth2/v1/token"

payload = {
    "grant_type": "client_credentials",
    "client_id": "102oklih8vrk3f4",
    "client_secret": "s9Az06XwSHuhjiOM_hkGSAi24-SHXo70oYN_f_BGPHEfPfZxw9exuW05Nh7i3bXX"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(token_url, data=payload, headers=headers)
response.raise_for_status()

token = response.json()["access_token"]



url = "https://api.zsapi.net/zpa/mgmtconfig/v1/admin/customers/288263573027684352/application"
params = {
  "page": 1,
  "pagesize": 100
}
headers = {
  "Authorization": token
}
response = requests.get(url, headers=headers, params=params)
""" print(response.json()) """
responsetext = response.text.splitlines()


""" print(json.dumps(response.json(), indent=1)) """

data = response.json()



with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["id", "name"])

    # Data rows
    for user in data["list"]:
        writer.writerow([user["id"], user["name"]])


test = requests.status_codes

print(test)
