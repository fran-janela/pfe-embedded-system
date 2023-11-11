import machine
 
sdaPIN=machine.Pin(18)  
sclPIN=machine.Pin(19)
 
i2c=machine.I2C(1,sda=sdaPIN, scl=sclPIN, freq=400000)   
 
devices = i2c.scan()
if len(devices) == 0:
 print('14CORE - i2c Finder / Scanner ')
 print("Error: No i2c device found, check properly the wiring!")
else:
 print('14CORE - i2c Finder / Scanner ')
 print('i2c devices found:',len(devices))
for device in devices:
 print("i2C Address: ",hex(device))