from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', 0x27)

lcd.write_string("Hello Shashwat")
sleep(3)

lcd.clear()
lcd.write_string("AI Booting")
lcd.cursor_pos = (1,4)
lcd.write_string("(o_o)")
