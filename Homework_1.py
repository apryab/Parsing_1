import requests
import time

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
url = "https://5ka.ru/special_offers/"
domain = "https://5ka.ru"
api_path = "/api/v2/special_offers/"
params = {
    'records_per_page': 20,
    #'categories': 443
}
response = requests.get(domain + api_path, headers = headers, params = params)
print(response.status_code)
products = []
temp_url = domain + api_path
while temp_url:
    response = requests.get(temp_url, headers=headers, params=params)
    data = response.json()
    params = {}
    temp_url = data['next']
    products.extend(data['results'])
    time.sleep(0.1)
print(products)

