import smbus
import time
 
# define I2C bus number
BUS_NUMBER = 1

# define device address
DEVICE_ADDR = 0x20

bus = smbus.SMBus(BUS_NUMBER)

# PULLUP all ports to enable button state readout
writeVal = 255
bus.write_byte(DEVICE_ADDR,writeVal)

while 1==1:
	#get current value from register
	currentVal = bus.read_byte(DEVICE_ADDR)
	
	#shift input bits (0-3) to output position (4-7) by shifting them left by 4 postions	
	writeVal = currentVal << 4

	#set input bits (0-3) to 1 to archive PULLUP
	writeVal = writeVal + 15

	#get only first 8 bits by doing modulo, this step can be ommited
	writeVal = writeVal % 256
	
	#write to register
	bus.write_byte(DEVICE_ADDR,writeVal)

	time.sleep(0.1)


