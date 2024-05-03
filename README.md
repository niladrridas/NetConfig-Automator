# Network Device Configuration Automation

## Project Description

This project is a Python-based automation script that uses the Netmiko library to interact with network devices. The script is designed to connect to a network device, execute configuration commands, and then disconnect. This automation can significantly reduce the time and effort required to configure network devices.

## Features

- Connects to a network device using SSH.
- Sends a list of configuration commands to the device.
- Handles exceptions and prints error messages.
- Disconnects from the device after sending the commands.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Open the `main.py` file in a text editor.
4. Replace the placeholder device information and commands with your actual device information and commands.
5. Save and close the file.
6. Run the script with the command `python main.py`.

## Requirements

This script requires Python 3 and the Netmiko library. 

## Installation

1. Ensure that Python 3 is installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).
2. Install the required Python library using pip, which is a package manager for Python. You can install pip by following the instructions on the [official pip installation guide](https://pip.pypa.io/en/stable/installation/).
3. Once pip is installed, navigate to the project directory in your terminal and run the following command to install the required library:

```bash
pip install -r requirements.txt