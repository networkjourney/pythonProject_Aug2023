from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException, SSHException
import xlrd
workbook123 = xlrd.open_workbook_xls(r"C:\Users\Njlinkedin\Music\deviceconfig123.xls")
sheet123 = workbook123.sheet_by_name("BANGALORE")
for fetchingdata in range(1,sheet123.nrows):
    hostname123 = sheet123.row(fetchingdata)[2].value
    print(hostname123)
    device_type123 = sheet123.row(fetchingdata)[3].value
    print(device_type123)
    singledevice123 = sheet123.row(fetchingdata)[1].value
    print(singledevice123)
    user123 = sheet123.row(fetchingdata)[4].value
    print(user123)
    pass123 = sheet123.row(fetchingdata)[5].value
    print(pass123)
    config123 = sheet123.row(fetchingdata)[7].value.splitlines()
    print(config123)
    clicommands123 = sheet123.row(fetchingdata)[8].value.splitlines()
    print(clicommands123)
    a = 1
    while a < 5:
        dev_details = {
            "password": input("enter the password " + hostname123 + "-" + singledevice123),
            "ip": singledevice123,
            "device_type": device_type123,
            "username": user123,
        }
        try:
            SSH123 = ConnectHandler(**dev_details)
            print("#" * 25)
            print(singledevice123 + " connected")
            print("#" * 25)
            show123 = SSH123.send_command("show run | i hostname")
            #print(show123)
            hostname123 = SSH123.find_prompt()
            print(hostname123)
            if ">" or "#" in hostname123:
                print("succesfully logged at " + str(a) + " attempt")
                for singlecli123 in clicommands123:
                    out123 = SSH123.send_command(singlecli123)
                    print(out123)
                    # take backup
                config123 = SSH123.send_config_set(config123)
                print(config123)
                #take backup
                break

        except NetmikoTimeoutException:
            print("device failing due to Timeout - " + singledevice123)
            #take backup of variable config123
            createemptyfolder123 = open(r"C:\Users\Njlinkedin\Music\3feb2024\Timeout" + ".txt", "a")
            createemptyfolder123.write(singledevice123 + "\n")
            createemptyfolder123.close()
        except NetmikoAuthenticationException:
            print("device failing due to Authentication - " + singledevice123)
            #take backup of variable config123
            createemptyfolder123 = open(r"C:\Users\Njlinkedin\Music\3feb2024\Authentication" + ".txt", "a")
            createemptyfolder123.write(singledevice123 + "\n")
            createemptyfolder123.close()
        except SSHException:
            print("device failing due to SSHException - " + singledevice123)
            #take backup of variable config123
            createemptyfolder123 = open(r"C:\Users\Njlinkedin\Music\3feb2024\SSHException" + ".txt", "a")
            createemptyfolder123.write(singledevice123 + "\n")
            createemptyfolder123.close()
        a += 1

print("JOB COMPLETED")
