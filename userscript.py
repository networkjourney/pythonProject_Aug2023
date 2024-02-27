import myparamikopackage
ssh_client = myparamikopackage.connect("172.16.24.254",22,"admin","cisco")
remote_connection123 = myparamikopackage.get_shell(ssh_client)
output123 = myparamikopackage.send_command(remote_connection123, "show run")
print(output123)
myparamikopackage.close(ssh_client)

