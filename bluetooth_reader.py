import asyncio
from bleak import BleakScanner, BleakClient

TARGET_DEVICE_NAME = "Nano33BLE_IMU"

async def discover_services_and_characteristics(client):
    print("Discovering services and characteristics...")
    for service in client.services:
        print(f"Service: {service.uuid}")
        for characteristic in service.characteristics:
            print(f"  Characteristic: {characteristic.uuid} - Properties: {characteristic.properties}")

async def read_y_degrees():
    print("Scanning for Bluetooth devices...")

    # Scan for devices
    devices = await BleakScanner.discover()
    target_device = None

    for device in devices:
        if device.name == TARGET_DEVICE_NAME:
            target_device = device
            break

    if not target_device:
        print(f"Device '{TARGET_DEVICE_NAME}' not found.")
        return

    print(f"Found target device '{TARGET_DEVICE_NAME}' with address: {target_device.address}")

    try:
        async with BleakClient(target_device.address, timeout=30.0) as client:
            if client.is_connected:
                print(f"Connected to {TARGET_DEVICE_NAME}!")

                # Discover and list all services and characteristics
                await client.get_services()
                await discover_services_and_characteristics(client)

                # Read the yDegreesCharacteristic value (assuming correct UUID format)
                Y_DEGREES_CHARACTERISTIC_UUID = "00000000-0000-0000-0000-000000222222"  # Replace with confirmed UUID if different
                try:
                    y_degrees_data = await client.read_gatt_char(Y_DEGREES_CHARACTERISTIC_UUID)
                    y_degrees = int.from_bytes(y_degrees_data, byteorder='little')
                    print(f"yDegrees: {y_degrees}")
                except Exception as e:
                    print(f"Failed to read yDegreesCharacteristic: {e}")
    except Exception as e:
        print(f"Failed to connect to {TARGET_DEVICE_NAME}: {e}")

# Run the function
asyncio.run(read_y_degrees())