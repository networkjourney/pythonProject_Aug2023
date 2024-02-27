from flask import Flask, request, render_template, Response
from netmiko import ConnectHandler

app = Flask(__name__)

# ...

# Add a new route to download the output
@app.route("/download_output", methods=["GET"])
def download_output():
    output_text = request.args.get("output_text")
    response = Response(output_text, content_type="text/plain")
    response.headers["Content-Disposition"] = "attachment; filename=output.txt"
    return response

# ...

# Function to read devices from a text file
def read_devices_from_file(filename):
    devices = []
    with open(filename, 'r') as file:
        for line in file:
            device_info = line.strip().split(',')
            if len(device_info) == 5:
                device = {
                    "device_type": device_info[1],
                    "ip": device_info[2],
                    "username": device_info[3],
                    "password": device_info[4],
                }
                devices.append((device_info[0], device))  # Store the name along with the device info
    return devices



# Read devices from the text file
devices = read_devices_from_file('push_config.txt')

@app.route("/")
def index():
    return render_template("index.html", devices=devices)

@app.route("/execute", methods=["POST"])
def execute_command():
    data = request.form
    device_name = data["device_name"]
    cli_command = data["cli_command"]

    # Find the selected device by name
    selected_device = next((device for name, device in devices if name == device_name), None)

    if selected_device:
        try:
            net_connect = ConnectHandler(**selected_device)
            output = net_connect.send_command(cli_command)
            net_connect.disconnect()
            return render_template("index.html", devices=devices, output=output)
        except Exception as e:
            return str(e)

    return "Device not found."



if __name__ == "__main__":
    app.run(debug=True)
