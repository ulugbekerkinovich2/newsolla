# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/convert?to=UZS&from=USD&amount=1"
#
# payload = {}
# headers= {
#   "apikey": "U7CXXvkaDQ3zUsFs6I1lfDnCIiQcWGsV"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)

# import requests
# import json
#
# url = "https://api.apilayer.com/scraper?url=https%3A%2F%2Fopenbudget.uz%2F"
#
# headers = {
#     "apikey": "U7CXXvkaDQ3zUsFs6I1lfDnCIiQcWGsV"
# }
#
# response = requests.get(url, headers=headers)
# status_code = response.status_code
# result = json.loads(response.text)
#
# # Get the "text" value from the "data" dictionary
# text = result["data"]["text"]
# print(text)
# '4633ab3ae1b0408e83ca88f8095c6230'