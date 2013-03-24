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

ledCounter = 1

while 1==1:
	#get current register state
	inputVal = bus.read_byte(DEVICE_ADDR)
	
	#shift counter bits left
	writeVal = ledCounter << 4

	#pullup input
	writeVal = writeVal + 15

	#negate bits 4-7 so only 1 led is lighted atm
	writeVal =writeVal ^ 240

	#write to register
	bus.write_byte(DEVICE_ADDR,writeVal)
	
	#multiply counter times 2
	ledCounter = ledCounter << 1
	#and cap at 16 (4 bits)
	if ledCounter == 16:
		ledCounter = 1


	#check if any button is pressed
	inputVal = inputVal & 15

	#if presses <> 15 rotate led 3 times faster
	if inputVal == 15:
		time.sleep(0.3)
	else:
		time.sleep(0.1)