from netmiko import ConnectHandler, redispatch
device123 = {
        "ip": "172.16.24.142",
        "username": "njauto1",
        "password": "cisco",
        "device_type": "terminal_server"
    }
ssh123 = ConnectHandler(**device123)
x = ssh123.send_command("ip r")
print(x)
print("Connect to Terminal server")
#second connections
ip123 = ["172.16.24.12", "172.16.24.18"]
for single in ip123:
    username1 = "admin"
    ssh123.write_channel("ssh -l " + username1 + " single")
    maxtrial = 5
    i = 1
    while i < maxtrial:
        ssh123.write_channel(input("enter the password: " + "\n"))
        out1234 = ssh123.read_channel()
        if ">" or "#" in out1234:
            ssh123.write_channel("enable" + "\n")
            ssh123.write_channel("cisco123" + "\n")
            ssh123.write_channel("show ip int br" + "\n")
            redispatch(ssh123, device_type="cisco_ios")
            ssh123.send_config_set("logging host 3.3.3.3")
            break
        else:
            print("failed ")
        i += 1