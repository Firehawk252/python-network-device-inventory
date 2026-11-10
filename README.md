# Network Device Inventory

A Python command-line application for managing network device inventory.

## Features

- Add network devices
- View devices
  - Filter devices by type
  - Display all devices
- Search devices by hostname or IP address
- Update device information
- Remove devices
- Save and load inventory using JSON
  - Automatically create inventory backups
  - Recover inventory from backup if the primary file is missing or corrupted

## Technologies

- Python
- JSON
- Git/GitHub

## Concepts Demonstrated

- Variables and data types
- Conditional statements and loops
- Lists and dictionaries
- Functions
- Exception handling
- File handling
- JSON serialization and deserialization
- Data validation
- Backup and recovery

## Project Structure
- `main.py` - Main application containing the inventory management functions and menu
- `devices.json` - Stores network device inventory data
- `devices_backup.json` - Backup copy of the inventory data

## Usage

- Clone the repository:
  - `git clone https://github.com/Firehawk252/python-network-device-inventory.git`
- Navigate to the project directory:
  - `cd python-network-device-inventory`
- Run the application:
  - `python main.py`
- Follow the command-line menu to manage your network device inventory
