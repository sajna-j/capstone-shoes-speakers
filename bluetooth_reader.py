import asyncio
from bleak import BleakScanner, BleakClient

TARGET_DEVICE_NAME = "Nano33BLE_IMU"
Y_DEGREES_CHARACTERISTIC_UUID = "26B10001-E8F2-537E-4F6C-D104768A1214"  # UUID for yDegreesCharacteristic

async def read_y_degrees():
    print("Scanning for Bluetooth devices...")

    # Scan for devices
    devices = await BleakScanner.discover()
    target_device = None

    # Find the device by name
    for device in devices:
        if device.name == TARGET_DEVICE_NAME:
            target_device = device
            break

    if not target_device:
        print(f"Device '{TARGET_DEVICE_NAME}' not found.")
        return

    print(f"Found target device '{TARGET_DEVICE_NAME}' with address: {target_device.address}")

    # Connect to the device
    async with BleakClient(target_device.address, timeout=30.0) as client:
        if client.is_connected:
            print(f"Connected to {TARGET_DEVICE_NAME}!")
            
            # Read the yDegreesCharacteristic value
            try:
                y_degrees_data = await client.read_gatt_char(Y_DEGREES_CHARACTERISTIC_UUID)
                # Convert the byte data to an integer (assuming it's a simple integer)
                y_degrees = int.from_bytes(y_degrees_data, byteorder='little')
                print(f"yDegrees: {y_degrees}")
            except Exception as e:
                print(f"Failed to read yDegreesCharacteristic: {e}")
        else:
            print(f"Failed to connect to {TARGET_DEVICE_NAME}")

# Run the reading function
asyncio.run(read_y_degrees())
