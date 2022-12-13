# import bluetooth
#
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
#
# def connect_to_arduino():
#
#     print("Searching for devices...")
#     nearby_devices = bluetooth.discover_devices()
#
#     num = 0
#     print("Select your device by entering its coresponding number...")
#     for i in nearby_devices:
#         num += 1
#     print(str(num) + ": " + bluetooth.lookup_name(i))
#     selection = int(input("> ")) - 1
#
#     bd_addr = nearby_devices[selection]
#     port = 1
#
#     print("You have selected " + bluetooth.lookup_name(nearby_devices[selection]))
#
#     sock.connect((bd_addr, port))
#
#
