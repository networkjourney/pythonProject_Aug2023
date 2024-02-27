from netmiko import ConnectHandler
import re
import csv
import os
multidevice = ["172.16.24.4","172.16.24.6"]
for singledevice in multidevice:
    server123 = {
        "device_type": "cisco_ios",
        "ip": singledevice,
        "username": "admin",
        "password": "cisco",
    }
    ssh123 = ConnectHandler(**server123)
    #fetch
    x = ssh123.send_command("show version")
    y = ssh123.send_command("show interfaces")
    #print(x)
    #pattern
    regexhostname123 = re.compile("(\S+)\s*uptime\s*is\s*")
    fetchedhostname123 = regexhostname123.findall(x)
    print(fetchedhostname123[0])
    regexuptime123 = re.compile("uptime\s*is\s*(.+)")
    fetcheduptime123 = regexuptime123.findall(x)
    print(fetcheduptime123[0])
    regexserialid123 = re.compile("Processor\s*board\s*ID\s*(\S+)")
    fetchedserial123 = regexserialid123.findall(x)
    print(fetchedserial123[0])
    regexipv4 = re.compile("\s*Internet\s*address\s*is\s*(\S+)/")
    fetchedipv4123 = regexipv4.findall(y)
    print(fetchedipv4123[0])
    regexmask123 = re.compile("\s*Internet\s*address\s*is\s*\S+/(\S+)")
    fetchedmask123 = regexmask123.findall(y)
    print(fetchedmask123[0])
    regexcurrentios123 = re.compile("\s*Version\s*(\S+)T5\s*,\s*RELEASE")
    fetchedios123 = regexcurrentios123.findall(x)
    print(fetchedios123[0])
    #check if csv is present in local directory or not
    filecheck123 = os.path.isfile(r"C:\Users\Njlinkedin\Music\BACKUP-regex\auditreport.csv")
    if filecheck123:
        # taking back to excel sheet
        with open(r"C:\Users\Njlinkedin\Music\BACKUP-regex\auditreport.csv", "a", newline="") as csv123:
            csvheaders123 = ["HOSTNAME", "IP ADDRESS", "SUBNET MASK", "CURRENT IOS VERSION", "UPTIME", "SERIAL ID"]
            writer123 = csv.DictWriter(csv123, fieldnames=csvheaders123)
            #writer123.writeheader()
            writer123.writerow({
                "HOSTNAME": fetchedhostname123[0],
                "SUBNET MASK": fetchedmask123[0],
                "CURRENT IOS VERSION": fetchedios123[0],
                "UPTIME": fetcheduptime123[0],
                "SERIAL ID": fetchedserial123[0],
                "IP ADDRESS": fetchedipv4123[0],
            })
    # taking back to excel sheet
    else:
        with open(r"C:\Users\Njlinkedin\Music\BACKUP-regex\auditreport.csv", "a", newline="") as csv123:
            csvheaders123 = ["HOSTNAME", "IP ADDRESS", "SUBNET MASK", "CURRENT IOS VERSION", "UPTIME", "SERIAL ID"]
            writer123 = csv.DictWriter(csv123, fieldnames=csvheaders123)
            writer123.writeheader()
            writer123.writerow({
                "HOSTNAME": fetchedhostname123[0],
                "SUBNET MASK": fetchedmask123[0],
                "CURRENT IOS VERSION": fetchedios123[0],
                "UPTIME": fetcheduptime123[0],
                "SERIAL ID": fetchedserial123[0],
                "IP ADDRESS": fetchedipv4123[0],
            })
print("CSV IS GENERATED")


