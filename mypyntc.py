from netmiko import ConnectHandler
cisco123 = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "username": "developer",
    "password": "lastorangerestoreball8876",
}
ssh123 = ConnectHandler(**cisco123)
fetch123 = ssh123.send_command("show ip int br")
print(fetch123)
config123 = ssh123.send_command_timing
print(config123)