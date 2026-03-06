from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

def idle():
    lcd.clear()
    lcd.write_string("Ask something")
    lcd.cursor_pos = (1,5)
    lcd.write_string("(o_o)")

def thinking():
    lcd.clear()
    lcd.write_string("Thinking...")
    lcd.cursor_pos = (1,5)
    lcd.write_string("(-_-)")

def show_text(text):
    lcd.clear()
    lcd.write_string(text[:16])
