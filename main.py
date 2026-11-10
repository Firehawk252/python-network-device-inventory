# Network Device Inventory
# A command-line application for managing network devices
# Firehawk252 11/10/2026
# v.1.0

import json
import shutil

def save_inventory(devices):
    with open("devices.json", "w") as file:
        json.dump(devices, file, indent=4)

    shutil.copy("devices.json", "devices_backup.json")

    print("Inventory saved successfully!")

# Function for adding a new device and its corresponding information
def add_device(devices):
    host = input("Enter a hostname: ")
    if host == "":
        print("Hostname cannot be empty.")
    else:
        found = False
        for device in devices:
            if device["Hostname"].lower() == host.lower():
                found = True
        if found:
            print("Hostname already exists.")
        else:
            ip = input("Enter an IP address: ")
            if ip == "":
                print("IP address cannot be empty.")
            else:
                found = False
                for device in devices:
                    if device["IP Address"] == ip:
                        found = True
                if found:
                    print("IP address already exists.")
                else:
                    device_type = input("Enter the device type (i.e., Switch, Router): ")
                    if device_type == "":
                        print("Device type cannot be empty.")
                    else:
                        location = input("Enter the device location: ")
                        if location == "":
                            print("Location cannot be empty.")
                        else:
                            device = {
                                "Hostname": host,
                                "IP Address": ip,
                                "Device Type": device_type,
                                "Location": location
                            }
                            devices.append(device)
                            save_inventory(devices)
                            print("Device successfully added!")

# Function for viewing device information
def view_devices(devices):
    if not devices:
        print("No devices found.")
    else:
        for number, device in enumerate(devices, start=1):
            print("Device #", number)
            print("Hostname: ", device["Hostname"])
            print("IP Address: ", device["IP Address"])
            print("Device Type: ", device["Device Type"])
            print("Location: ", device["Location"])
            print("---------------------------")
        print("Total Number of Devices: ", len(devices), "\n")

# Function for searching devices
def search_devices(devices):
    host_input = input("Enter the hostname or IP address: ")
    found = False
    for device in devices:
        if device["Hostname"].lower() == host_input or device["IP Address"] == host_input:
            found = True
            print("Hostname: ", device["Hostname"])
            print("IP Address: ", device["IP Address"])
            print("Device Type: ", device["Device Type"])
            print("Location: ", device["Location"])
    if not found:
        print("Device not found.")

# Function for filtering devices during viewing
def filter_devices(devices):
    print("View devices by what type?")
    print("1. Router")
    print("2. Switch")
    print("3. Enter manual info")
    choice = int(input("Enter a choice: "))

    found = False
    count = 0

    if choice == 1:
        for device in devices:
            if device["Device Type"].lower() == "router":
                found = True
                count += 1
                print("Hostname: ", device["Hostname"])
                print("IP Address: ", device["IP Address"])
                print("Device Type: ", device["Device Type"])
                print("Location: ", device["Location"])
                print("---------------------------")
        print("Total Number of Devices:", count, "\n")
        if not found:
            print("Device not found.")
    elif choice == 2:
        for device in devices:
            if device["Device Type"].lower() == "switch":
                found = True
                count += 1
                print("Hostname: ", device["Hostname"])
                print("IP Address: ", device["IP Address"])
                print("Device Type: ", device["Device Type"])
                print("Location: ", device["Location"])
                print("---------------------------")
        print("Total Number of Devices:", count, "\n")
        if not found:
            print("Device not found.")

    elif choice == 3:
        type_input = input("Enter the device type: ").lower()
        for device in devices:
            if device["Device Type"].lower() == type_input:
                found = True
                count += 1
                print("Hostname: ", device["Hostname"])
                print("IP Address: ", device["IP Address"])
                print("Device Type: ", device["Device Type"])
                print("Location: ", device["Location"])
                print("---------------------------")
        print("Total Number of Devices:", count, "\n")
        if not found:
            print("No matching devices found.")
    else:
        print("Invalid choice.")

# Function for updating device information
def update_device(devices):
    host_input = input("What is the hostname of the device you want to update? ").lower()
    found = False
    for device in devices:
        if device["Hostname"].lower() == host_input:
            found = True
            print("1. Hostname")
            print("2. IP Address")
            print("3. Device Type")
            print("4. Location")
            try:
                update_choice = int(input("What value is being updated? "))
            except ValueError:
                print("Invalid choice.")
            else:
                if update_choice == 1:
                    host_change = input("Enter the new hostname: ").lower()
                    if host_change == "":
                        print("Hostname cannot be empty.")
                    else:
                        duplicate = False
                        for existing_device in devices:
                            if existing_device["Hostname"].lower() == host_change:
                                if existing_device is not device:
                                    duplicate = True
                        if duplicate:
                            print("Hostname already exists.")
                        else:
                            device["Hostname"] = host_change
                            print("New hostname: ", device["Hostname"])

                elif update_choice == 2:
                    ip_change = input("Enter the new IP address: ")
                    if ip_change == "":
                        print("IP address cannot be empty.")
                    else:
                        duplicate = False
                        for existing_device in devices:
                            if existing_device["IP Address"] == ip_change:
                                if existing_device is not device:
                                    duplicate = True
                        if duplicate:
                            print("IP address already exists.")
                        else:
                            device["IP Address"] = ip_change
                            print("New IP address: ", device["IP Address"])

                elif update_choice == 3:
                    type_change = input("Enter the new device type: ")
                    if type_change == "":
                        print("Device type cannot be empty.")
                    else:
                        device["Device Type"] = type_change
                        print("New device type: ", device["Device Type"])

                elif update_choice == 4:
                    location_change = input("Enter the new location: ")
                    if location_change == "":
                        print("Location cannot be empty.")
                    else:
                        device["Location"] = location_change
                        print("New location: ", device["Location"])

                else:
                    print("Invalid choice.")
                save_inventory(devices)
    if not found:
        print("Device not found.")
# Function for removing a device
def remove_device(devices):
    rem_input = input("Enter the device you want to remove: ").lower()
    found = False
    for device in devices:
        if device["Hostname"].lower() == rem_input:
            found = True
            while True:
                confirm = input("Are you sure you want to remove this device? (y/n) ").lower()
                if confirm == "y":
                    devices.remove(device)
                    save_inventory(devices)
                    print("Device successfully removed!")
                    break
                elif confirm == "n":
                    print("Device removal cancelled.")
                    break
                else:
                    print("Invalid response. Try again.")
    if not found:
        print("Device not found.")

def main():
    print("==================================")
    print("     Network Device Inventory")
    print("==================================")

# Allow users to add network devices to an inventory and keep those devices available while the application is running

    try:
        with open("devices.json", "r") as file:
            devices = json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. Checking for backup...")
        try:
            with open("devices_backup.json", "r") as file:
                devices = json.load(file)
            print("Inventory successfully recovered from backup!")
            save_inventory(devices)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Backup is missing or corrupted. Starting with empty inventory.")
            devices = []
    except json.JSONDecodeError:
        print("Inventory file is corrupted. Attempting backup recovery...")
        try:
            with open("devices_backup.json", "r") as file:
                devices = json.load(file)
            print("Inventory successfully recovered from backup!")
            save_inventory(devices)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Backup is missing or corrupted. Starting with empty inventory.")
            devices = []


# Allow users to navigate the inventory application through a command-line menu
# The menu will repeat until the user exits

    while True:

        print("1. Add Device")
        print("2. View Devices")
        print("3. Search Devices")
        print("4. Update Device")
        print("5. Remove Device")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 1:
            add_device(devices)

        elif choice == 2:
            while True:
                print("1. View all devices")
                print("2. Filter devices")
                print("3. Return to main menu")

                try:
                    new_choice = int(input("Enter your choice: "))
                    if new_choice == 1:
                        view_devices(devices)
                    elif new_choice == 2:
                        filter_devices(devices)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid choice.")

        elif choice == 3:
            search_devices(devices)

        elif choice == 4:
            update_device(devices)

        elif choice == 5:
            remove_device(devices)

        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid Option.")

main()