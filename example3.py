from netmiko import ConnectHandler
import time
from netmiko.exceptions import NetmikoAuthenticationException, NetMikoTimeoutException, SSHException
#from netmiko.ssh_exception import NetmikoAuthenticationException, NetMikoTimeoutException, SSHException
ip_add = ip_list = ["172.16.24.25", "172.16.24.27", "172.16.24.16","172.16.24.20", "172.16.24.18", "172.16.24.19"]
for i in ip_add:
    a = 1
    while a <= 5:
        try:
            device_info = {
                'device_type': 'cisco_ios',
                'ip': i,
                'username': "admin",
                'password': input("enter the password " + i + ": "),
                'secret': 'cisco'
            }
            time.sleep(5)
            ssh_session = ConnectHandler(**device_info)
            ssh_session.enable()
            out123 = ssh_session.find_prompt()
            print(out123)
            if ">" or "#" in out123:
                print(" login is successful " + i)
                break
            else:
                pass
        except NetmikoAuthenticationException:
            print("trying again")
        a = a + 1
        print(a)
