import os
import random
import board
import time


from adafruit_pyportal import PyPortal

pyportal = PyPortal(status_neopixel=board.NEOPIXEL, default_bg="/PyCon2019Badge.bmp")

reset_active = False

def in_region(region, point):
    rx, ry, rw, rh = region
    x, y, _ = point

    return (
        x > rx and x < rx + rw and
        y > ry and y < ry + rh
    )

def main_screen():
    pyportal.set_background('PyCon2019Badge.bmp')

def show_contact():
    pyportal.set_background('QR.bmp')

touchpoints = {
    'contact': {
        'region': (0, 120, 320, 120),
        'action': show_contact,
    }
}

# main loop
while True:
    touch = pyportal.touchscreen.touch_point
    if touch:
        print(touch)
        if reset_active:
            reset_active = False
            main_screen()
        else:
            for k, touchpoint in touchpoints.items():
                if in_region(touchpoint['region'], touch):
                    reset_active = True
                    touchpoint['action']()


        # Wait for no touch event to stop duplicate touchs
        while pyportal.touchscreen.touch_point:
            time.sleep(0.9)