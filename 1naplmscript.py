import requests

url = "https://sandbox-sdwan-2.cisco.com:443/dataservice/device/monitor"

payload = {}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpSRyFfWXc5MTlfODM=',
  'Cookie': 'JSESSIONID=io_97SbLp0ylC3ZMtzH6N_adAFL1fyublbBBvzWv.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)
