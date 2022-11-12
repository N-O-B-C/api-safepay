import requests

#url = "https://safe-payy.herokuapp.com"
header = {'content-type': 'application/json', 'x-access-token': '5443b693E341cb0ab695Xb8'}
url = "https://safe-payy.herokuapp.com/api/v1/safepay/querypayment/initiated"

response = requests.get(url, headers=header)

if response.status_code == 200:
    print(response.text)

else:
    print(f"Error:{response.status_code}")