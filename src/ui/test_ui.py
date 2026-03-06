import time
import lcd_controller

lcd_controller.idle()
time.sleep(3)

lcd_controller.thinking()
time.sleep(3)

lcd_controller.show_text("Hello Human")
