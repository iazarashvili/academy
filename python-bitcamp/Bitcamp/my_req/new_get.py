import requests

payload = {
  "brandIds": [],
  "categorySlug": None,
  "categoryId": None,
  "modelIds": [],
  "features": {},
  "merchantSlugs": [],
  "sortType": 1,
  "sortBy": 4,
  "pageNumber": 1,
  "pageSize": 48,
  "setIds": [
    4988
  ],
  "darkStoreId": 50,
  "deliveryTypes": None
}

headers = {'content-type': 'application/json'}
r = requests.post('https://mercury.staging.extra.ge/search/billie-jean', json=payload)
print(r.headers)
print(r.text)
