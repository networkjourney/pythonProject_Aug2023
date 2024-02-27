#auto detect
from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_autodetect import SSHDetect
multidevice = ["172.16.24.18", "172.16.24.12"]
for signledevice123 in multidevice:
    device123 = {
        "ip": signledevice123,
        "username": "admin",
        "password": "cisco",
        "device_type": "autodetect"
    }
    ssh123 = SSHDetect(**device123)
    device_type = ssh123.autodetect()
    print(device_type)
    if device_type == "cisco_ios":
        ciscodevice123 = {
            "ip": signledevice123,
            "username": "admin",
            "password": "cisco",
            "device_type": device_type
        }
        ssh123 = ConnectHandler(**ciscodevice123)
        fetch123 = ssh123.send_command("show ip int br")
        print(fetch123)
        #copy123 = ssh123.file_transfer
    elif device_type == "panos":
        pandevice123 = {
            "ip": signledevice123,
            "username": "admin",
            "password": "cisco",
            "device_type": device_type
        }
        ssh123 = ConnectHandler(**pandevice123)
        fetch123 = ssh123.send_command("show interface management")
        copy123 = ssh123.file_transfer("panos.py")
    elif device_type == "forti":
        print("forti")

    elif device_type == "f5":
        print("f5")

    else:
        print("device type found is no ssh-based !")

