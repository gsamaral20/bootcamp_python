import requests

# requests.get # select

# requests.post # create

# requests.put # update

# requests.delete # delete

URL = "https://www.mercadolivre.com.br"
response = requests.get(url=URL)
data = response.json()
print(data)