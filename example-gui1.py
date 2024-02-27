import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from netmiko import ConnectHandler
from tkinter import scrolledtext

# Define global variables to store the command outputs
output1 = ""
output2 = ""
output3 = ""

# Function to populate the IP, username, and password fields based on device selection
def on_device_select(event):
    selected_device = device_combobox.get()
    for device in device_details:
        if device[0] == selected_device:
            ip_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            ip_entry.insert(0, device[1])
            username_entry.insert(0, device[2])
            password_entry.insert(0, device[3])

def get_device_info():
    global output1, output2, output3  # Declare these variables as global
    ip_address = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    getclicommand1 = cli1_entry.get()
    getclicommand2 = cli2_entry.get()
    selected_cli_command = cli_combobox.get()

    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**cisco_device)
    except Exception as e:
        result_label.config(text=f"Connection Error: {str(e)}")
        return

    try:
        findprompt123 = net_connect.find_prompt()
        print(findprompt123)
        if ">" in findprompt123 or "#" in findprompt123:
            net_connect.enable()
            findprompt123 = net_connect.find_prompt()
            print(findprompt123)
            output1 = net_connect.send_command(getclicommand1)
            output2 = net_connect.send_command(getclicommand2)
            output3 = net_connect.send_command(selected_cli_command)
            result_label0.config(text="#" * 10 + f" Output for CLI Command " + getclicommand1.upper() + " " + "#" * 10)
            result_label1.config(text=f"{output1}" + "\n")
            result_label2.config(text="#" * 10 + f" Output for CLI Command " + getclicommand2.upper() + " " + "#" * 10)
            result_label3.config(text=f"{output2}" + "\n")
            result_label4.config(text="#" * 10 + f" Output for Selected CLI Command " + selected_cli_command.upper() + " " + "#" * 10)
            result_label5.config(text=f"{output3}" + "\n")
            net_connect.disconnect()
        else:
            print("enable mode")
    except Exception as e:
        result_label.config(text=f"Command Error: {str(e)}")

def save_output(output, filename):
    try:
        with open(filename, 'w') as file:
            file.write(output)
        messagebox.showinfo("File Saved", f"Output saved to {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {str(e)}")

def save_output1():
    save_output(output1, "output1.txt")

def save_output2():
    save_output(output2, "output2.txt")

def save_output3():
    save_output(output3, "output3.txt")

window = tk.Tk()
window.title("Netmiko NetworkJourney.com")
window.geometry("800x400")  # Set the window size

font = ("Calibri", 11)

ip_label = tk.Label(window, text="Device IP Address:", font=font)
username_label = tk.Label(window, text="Username:", font=font)
password_label = tk.Label(window, text="Password:", font=font)
device_label = tk.Label(window, text="Select Device:", font=font)
cli1_label = tk.Label(window, text="CLI Command 1:", font=font)
cli2_label = tk.Label(window, text="CLI Command 2:", font=font)
cli_label = tk.Label(window, text="Select CLI Command:", font=font)

ip_entry = tk.Entry(window, font=font)
username_entry = tk.Entry(window, font=font)
password_entry = tk.Entry(window, show="*", font=font)
cli1_entry = tk.Entry(window, font=font)
cli2_entry = tk.Entry(window, font=font)

result_label0 = tk.Label(window, text="", font=font)
result_label1 = tk.Label(window, text="", font=font)
result_label2 = tk.Label(window, text="", font=font)
result_label3 = tk.Label(window, text="", font=font)
result_label4 = tk.Label(window, text="", font=font)
result_label5 = tk.Label(window, text="", font=font)

device_details = []
try:
    with open('tkinter.txt', 'r') as file:
        for line in file:
            device_details.append(line.strip().split(','))
except FileNotFoundError:
    device_details = []

show_commands = [
    "show ip int br",
    "show ip route",
    "show arp",
    "show clock",
    "show ip ospf nei",
    "show ip bgp nei",
    "show run | i hostname"
]

device_names = [device[0] for device in device_details]
device_combobox = ttk.Combobox(window, values=device_names, font=font)
device_combobox.bind("<<ComboboxSelected>>", on_device_select)

cli_combobox = ttk.Combobox(window, values=show_commands, font=font)

connect_button = tk.Button(window, text="Connect", command=get_device_info, font=font)

ip_label.grid(row=0, column=0)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
device_label.grid(row=3, column=0)
cli1_label.grid(row=4, column=0)
cli2_label.grid(row=5, column=0)
ip_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)
device_combobox.grid(row=3, column=1)
cli1_entry.grid(row=4, column=1)
cli2_entry.grid(row=5, column=1)
cli_label.grid(row=6, column=0)
cli_combobox.grid(row=6, column=1)
connect_button.grid(row=7, column=0, columnspan=2)
result_label0.grid(row=8, column=0, columnspan=2)
result_label1.grid(row=9, column=0, columnspan=2)
result_label2.grid(row=10, column=0, columnspan=2)
result_label3.grid(row=11, column=0, columnspan=2)
result_label4.grid(row=12, column=0, columnspan=2)
result_label5.grid(row=13, column=0, columnspan=2)

# Function to save output to a file
def save_output(output, filename):
    try:
        with open(filename, 'w') as file:
            file.write(output)
        messagebox.showinfo("File Saved", f"Output saved to {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {str(e)}")

# Create buttons to save output
save_button1 = tk.Button(window, text="Save Output 1", command=save_output1, font=font)
save_button2 = tk.Button(window, text="Save Output 2", command=save_output2, font=font)
save_button3 = tk.Button(window, text="Save Output 3", command=save_output3, font=font)

# Add save buttons to the GUI
save_button1.grid(row=14, column=0, columnspan=2)
save_button2.grid(row=15, column=0, columnspan=2)
save_button3.grid(row=16, column=0, columnspan=2)

# Function to save the selected CLI command output to a file
def save_selected_output():
    selected_output = result_label5.cget("text")  # Get the selected CLI command output
    save_output(selected_output, "selected_output.txt")

# Create a button to save the selected CLI command output
save_selected_button = tk.Button(window, text="Save Selected Output", command=save_selected_output, font=font)
save_selected_button.grid(row=17, column=0, columnspan=2)

# Start the GUI main loop
window.mainloop()
