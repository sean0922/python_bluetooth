import bluetooth


print("Looking for bluetooth ")
nearby_devices = bluetooth.discover_devices(lookup_names=True)

for addr,name in nearby_devices:
    print("addr :",addr)
    print("name :",name)
'''
sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )
bd_addr = "18:95:52:07:0D:F1"
port = 0x1001
sock.connect((bd_addr, port))
sock.close()
'''