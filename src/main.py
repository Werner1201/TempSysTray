from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw, ImageColor, ImageFont
import threading
import multiprocessing
import time
import json
import requests
import random

location = "Duque de Caxias"


def create_image(temperatura: int) -> None:
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


def get_weather() -> int:
    key = "610f0cdf37062926c9536ed9f7621e23"
    locationFormated = location.replace(" ", "+")
    try:
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(locationFormated, key))
        obj = r.json()
        return int(obj['main']['temp'])
    except:
        return int("00")


def create_icon() -> SysTrayIcon:
    weather = get_weather()
    create_image(weather)
    systray = SysTrayIcon(
        "temp.ico", "Temperatura em {}".format(location))
    return systray


def main() -> None:
    tray = create_icon()
    tray.start()
    while True:
        time.sleep(3600)
        create_image(get_weather())
        tray.update(icon="temp.ico")
    tray.shutdown()
    pass


main()
