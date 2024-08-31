# import resquest
import requests
# define url
url = 'https://quotes.toscrape.com/'

# get respons: .get()
resp = requests.get(url)
print(resp)

print(resp.status_code)  # 200 status code = successful
