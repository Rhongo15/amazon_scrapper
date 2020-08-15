from selectorlib import Extractor
import requests 
import json 

#getting input from user and appending it to the url
item = input()
item = list(item.split(' '))
item = '+'.join(item)
url = 'https://www.amazon.com/s?k=' + item

#yml file containing the selectors needed to extract data
e = Extractor.from_yaml_file('search_results.yml')

#function to scrape the required data
def data_extractor(url):  
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    print("Scraping Data...")
    r = requests.get(url, headers=headers) 
    return e.extract(r.text)

#calling above function
data = data_extractor(url) 

#printing results in JSON structure
for product in data['products']:
    r = json.dumps(product)
    loaded_r = json.loads(r)
    print(json.dumps(loaded_r, indent=1))
