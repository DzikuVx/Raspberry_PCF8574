import smbus
import time
 
# define I2C bus number
BUS_NUMBER = 1

# define device address
DEVICE_ADDR = 0x20

bus = smbus.SMBus(BUS_NUMBER)
writeVal = 255
 
bus.write_byte(DEVICE_ADDR,writeVal)

while 1==1:
	currentVal = bus.read_byte(DEVICE_ADDR)
	inputVal = 255 - currentVal
	writeVal = (currentVal * 16) + 15

	print inputVal

	bus.write_byte(DEVICE_ADDR,writeVal)
	time.sleep(0.1)


