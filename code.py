import requests
import pandas as pd

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
headers = {
    "accept": "application/json",
    "Authorization": "Your API Bearer Token"
}
response = requests.get(url, headers=headers)
data = response.json
df = pd.json_normalize(data())
print(df)