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
usd_brl = float(df["USDBRL.high"][0])
print(usd_brl)

brl = float(input("How much money (R$) do you have?\n"))
convertion = brl / usd_brl
print("With R${:.2f} you can buy ${:.2f} currently".format(brl, convertion))
