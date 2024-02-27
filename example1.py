from netmiko import ConnectHandler, redispatch
#import textfsm
multidevice = ["172.16.24.58"]
for singledevice in multidevice:
    server123 = {
        "device_type": "f5_tmsh",
        "ip": singledevice,
        "username": "root",
        "password": "networkjourney",
    }
    ssh123 = ConnectHandler(**server123)
    #pre-checks
    config123 = ssh123.send_config_from_file("172.16.24.58configpush.txt")
    print(config123)
    multiplecommands123 = ["list ltm node"]
    for singlecommand123 in multiplecommands123:
        fetch123 = ssh123.send_command(singlecommand123)#, #use_textfsm=True)
        print(fetch123)
        #take backup in text
        with open(singledevice + ".txt", "a") as backup1:
            backup1.write(fetch123)
