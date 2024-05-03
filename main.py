from netmiko import ConnectHandler

# Function to connect to a network device
def connect_to_device(device_info):
    try:
        connection = ConnectHandler(**device_info)
        print(f"Connected to {device_info['host']}")
        return connection
    except Exception as e:
        print(f"Failed to connect to {device_info['host']}: {str(e)}")
        print("Common causes of this problem are:")
        print("1. Incorrect hostname or IP address.")
        print("2. Wrong TCP port.")
        print("3. Intermediate firewall blocking access.")
        print(f"Device settings: {device_info['device_type']} {device_info['host']}:{device_info.get('port', 22)}")
        return None

# Function to send configuration commands to a device
def configure_device(connection, commands):
    try:
        output = connection.send_config_set(commands)
        print(output)
        print("Configuration applied successfully.")
    except Exception as e:
        print(f"Failed to configure device: {str(e)}")

# Main function
def main():
    # Device information (example - replace with actual device details)
    device_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'password',
    }

    # Sample configuration commands (replace with actual configuration)
    commands = [
        'interface GigabitEthernet0/1',
        'description Connection to LAN',
        'ip address 192.168.1.1 255.255.255.0',
        'no shutdown',
        'exit'
    ]

    # Connect to the device
    connection = connect_to_device(device_info)
    if connection:
        # Apply configuration to the device
        configure_device(connection, commands)
        # Disconnect from the device
        connection.disconnect()

if __name__ == "__main__":
    main()