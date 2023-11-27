import requests
import json
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY5NDk4Mzk4MywiaWF0IjoxNjk0OTgwMzgzLCJqdGkiOiJmMzZlOTg5Yi1mMTYyLTRjNTItYTZiOC03OGU5N2IyYWIzZWUiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.rViNH_r4jsiikscoKov8ThRZZSr6LJmgLz9eTvm0fwvkLrUeQhDyno3S7D_1JctSP4kipBPIKFPMdSdgmNKi2rLwex0QPOoL2RTCZcgGGfhzLmi9gX9yBkViph5X3n51Iqovq_S5KWNm2HQx7kyNozXD4Yf2aJHeKHwccXTe44m2LC3SfB4joPEJ8hlVDEIFVxEdR6T7Om8-lkAQeIUx2BQRJPUWieOpOM4yMWdbMEis1s6CDQ99GIHTQOLiBJ2YmRQBWcqv2v1aVjm-7zls0FB8z60P8_nAJqypt--WW0sai0OC55nZXrVJpp2ZfQuD6UhmJPizd84nGrSodEgwWg',
  'Cookie': 'JSESSIONID=1gwq5wh0kwko7h96umix1va7v'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

y = response.text

# Parse the JSON data
data = json.loads(y)
# Extract and print descriptions
for item in data['response']:
    description = item['description']
    print(description)
    #################################sddsaasddsaasdsda
