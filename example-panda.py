from netmiko import ConnectHandler
import pandas as pd
import matplotlib.pyplot as plt

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.24.38',
    'username': "admin",
    'password': "cisco",
}

# Connect to the device
try:
    net_connect = ConnectHandler(**device)
    print("Connected to the device.")
except Exception as e:
    print(f"Connection Error: {str(e)}")
    exit()

# Send a command to retrieve interface information (e.g., 'show ip interface brief')
command = 'show ip interface brief'
output = net_connect.send_command(command)

# Close the SSH connection
net_connect.disconnect()

# Process the output using Pandas
lines = output.splitlines()
data = [line.split() for line in lines[1:]]  # Skip the header line
columns = ['Interface', 'IP Address', 'OK?', 'Method', 'Status', 'Protocol']

# Create a DataFrame from the parsed data
df = pd.DataFrame(data, columns=columns)

# Filter the DataFrame to select interfaces that are in the "up" state
filtered_df = df[df['Status'] == 'up']

# Display the filtered DataFrame
print(filtered_df)

# Create a bar chart to visualize the distribution of interface statuses
status_counts = df['Status'].value_counts()
status_counts.plot(kind='bar', xlabel='Interface Status', ylabel='Count', title='Interface Status Distribution')

# Add labels to the bars
for i, count in enumerate(status_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.show()
