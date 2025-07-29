from picamera2 import Picamera2
from time import sleep, strftime
import os
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
import ST7789

# GPIO Pin Setup (will update this later according to the pins I end up using!)
SHUTTER_BUTTON = 17  
BUTTONS = [5, 6, 13, 19]  

GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTTER_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for btn in BUTTONS:
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ST7789 Display Setup
disp = ST7789.ST7789(
    height=240,
    width=240,
    rotation=180,
    port=0,
    cs=0,
    dc=9,
    backlight=19,
    spi_speed_hz=80_000_000
)
disp.begin()

def display_text(text):
    image = Image.new("RGB", (240, 240), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 100), text, font=font, fill=(255, 255, 255))
    disp.display(image)

# Camera Setup
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

display_text("Ready!")

try:
    while True:
        if GPIO.input(SHUTTER_BUTTON) == GPIO.LOW:
            filename = f"/home/pi/Pictures/{strftime('%Y%m%d-%H%M%S')}.jpg"
            display_text("Capturing...")
            picam2.capture_file(filename)
            display_text("Saved!")

            sleep(1)
            display_text("Ready!")
        sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    disp.cleanup()
