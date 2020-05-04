from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw, ImageColor, ImageFont
import threading
import multiprocessing
import time
import json
import requests
import random


def setup(icon):
    icon.visible = True
    pass


def create_image(temperatura):
    # Generate an image
    width = 40
    height = 25
    color1 = "#00000000"
    font = ImageFont.truetype('arial.ttf', 20)

    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.text((0, 0), "{}C".format(temperatura),
            font=font, fill=(255, 255, 255))
    image.save("temp.ico")
    pass


def exit_action(icon):
    icon.shutdown()


def get_weather():
    key = "610f0cdf37062926c9536ed9f7621e23"
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Duque+de+Caxias&APPID={}&units=metric'.format(key))
    obj = r.json()
    return int(obj['main']['temp'])


def create_icon():
    create_image(get_weather())
    menu_options = (("Exit", None, exit_action),)
    systray = SysTrayIcon("temp.ico", "Example tray icon", menu_options)
    return systray


def main():
    tray = create_icon()
    tray.start()
    while True:
        time.sleep(3600)
        create_image(get_weather())
        tray.update(icon="temp.ico")
    pass


main()
