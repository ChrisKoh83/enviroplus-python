#!/usr/bin/env python

import ST7735
from PIL import Image, ImageDraw, ImageFont

print("""lcd.py - Hello, World! example on the 0.96" LCD.

Press Ctrl+C to exit!

""")

# Create LCD class instance.
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display.
disp.begin()

# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

# New canvas to draw on.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Text settings.
font_size = 25
font = ImageFont.truetype("fonts/Asap/Asap-Bold.ttf", font_size)
text_colour = (255, 255, 255)
back_colour = (0, 170, 170)

message = "Hello, World!"
size_x, size_y = draw.textsize(message, font)

# Calculate text position
x = (WIDTH - size_x) / 2
y = (HEIGHT / 2) - (size_y / 2)

# Draw background rectangle and write text.
draw.rectangle((0, 0, 160, 80), back_colour)
draw.text((x, y), message, font=font, fill=text_colour)
disp.display(img)

# Keep running.
try:
    while True:
        pass

# Turn off backlight on control-c
except KeyboardInterrupt:
    disp.set_backlight(0)
