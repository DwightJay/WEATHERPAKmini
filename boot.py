# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

import machine
import bme280
import time
import ssd1306

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2)) 
screen = ssd1306.SSD1306_I2C(128, 64, i2c, 60) 

while True:
	time.sleep(5)
	print(bme.values)
	screen.poweroff()
	screen.poweron()
	i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2))
	screen = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
	screen.text("WEATHERPAKmini   CES",0,0)
	screen.text((''.join(str(y) for x in bme.values[0] for y in x if len(x) > 0)),0,10)
	screen.text((''.join(str(y) for x in bme.values[1] for y in x if len(x) > 0)),0,20)
	screen.text((''.join(str(y) for x in bme.values[2] for y in x if len(x) > 0)),0,30)
	screen.show()
