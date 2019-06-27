# -*- encoding: utf-8 -*-

import time
import math
import random
import argparse
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from neopixel import *
from gpiozero import Button
from random import randint
from time  import sleep
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# OLED
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

 # Schreibe eine Zeile aufs Display
def writeToDisplay(text, x=0, y=0, size=8):

    # Get drawing object to draw on image.
    image = Image.new('1', (disp.width, disp.height))
    draw = ImageDraw.Draw(image)

    #font = ImageFont.load_default()
    font = ImageFont.truetype('/usr/share/fonts/truetype/piboto/Piboto-Regular.ttf', size=size)

    draw.text((x, y), text, font=font, fill=255)
    disp.image(image)
    disp.display()

writeToDisplay("Hallo Velo", x=0, y=5, size=16)


# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 25     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

colorgreen = Color(255, 0, 0)
colorred = Color(0, 255, 0)
colorblue = Color(0, 0, 255)
coloryellow = Color(255, 255, 0)
colororange = Color(69, 255, 0)
aus = Color(0, 0, 0)
startbutton = Button(25, pull_up=False)
player1 = Button(23, pull_up=False)
player2 = Button(5, pull_up=False)
player3 = Button(6, pull_up=False)
player4 = Button(26, pull_up=False)


led = -1
led0 = 0
led1 = 1
led2 = 2
led3 = 3
led4 = 4
led5 = 5
led6 = 6
led7 = 7
ledall = led0, led1, led2, led3, led4, led5, led6, led7


GPIO.setup(24, GPIO.OUT)
#for led in range(8):
    #print (led)
    #strip.setPixelColor(led, color)
    #strip.setPixelColor(led-2, aus)
    #strip.show()
    #time.sleep(0.5)


def allesAus():
    for led in range(8):
        strip.setPixelColor(led, aus)

def alleLedsG():
    for led in range(8):
        strip.setPixelColor(led, colorgreen)
        led = led + 1

def animation():
    GPIO.output(24, GPIO.LOW)
    strip.setPixelColor(led0, colorred)
    strip.setPixelColor(led1, colorred)
    strip.setPixelColor(led7, colorred)
    strip.setPixelColor(led6, colorred)
    strip.show()
    allesAus()
    time.sleep(1)
    strip.setPixelColor(led1, colororange)
    strip.setPixelColor(led2, colororange)
    strip.setPixelColor(led6, colororange)
    strip.setPixelColor(led5, colororange)
    strip.show()
    allesAus()
    time.sleep(1)
    strip.setPixelColor(led2, coloryellow)
    strip.setPixelColor(led3, coloryellow)
    strip.setPixelColor(led4, coloryellow)
    strip.setPixelColor(led5, coloryellow)
    strip.show()
    time.sleep(1)
    strip.show()
    alleLedsG()
    strip.show()
    #GPIO.output(24, GPIO.HIGH)
    time.sleep(1)
    #GPIO.output(24, GPIO.LOW)
    print(bcolors.OKGREEN + '''\n\n\n                                                                                           ┌───┐┌┐░░░░░░┌┐░
                                                                                           │┌─┐├┘└┐░░░░┌┘└┐
                                                                                           │└──┼┐┌┼──┬─┼┐┌┘
                                                                                           └──┐││││┌┐│┌┘││░
                                                                                           │└─┘││└┤┌┐││░│└┐
                                                                                           └───┘└─┴┘└┴┘░└─┘
''' + bcolors.ENDC)
    print('\n\n')
    allesAus()
    strip.show()
    GPIO.output(24, GPIO.LOW)


def player1_win():
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
    strip.setPixelColor(0, colorblue)
    strip.setPixelColor(1, colorblue)
    strip.setPixelColor(2, colorblue)
    strip.setPixelColor(3, colorblue)
    strip.setPixelColor(4, colorblue)
    strip.setPixelColor(5, colorblue)
    strip.setPixelColor(6, colorblue)
    strip.setPixelColor(7, colorblue)
    print(spieler1 + " war am flinksten!")
    strip.show()


def player2_win():
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
    strip.setPixelColor(0, colorred)
    strip.setPixelColor(1, colorred)
    strip.setPixelColor(2, colorred)
    strip.setPixelColor(3, colorred)
    strip.setPixelColor(4, colorred)
    strip.setPixelColor(5, colorred)
    strip.setPixelColor(6, colorred)
    strip.setPixelColor(7, colorred)
    print(spieler2 + " war am flinksten!")
    strip.show()


def player3_win():
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
    strip.setPixelColor(0, colorgreen)
    strip.setPixelColor(1, colorgreen)
    strip.setPixelColor(2, colorgreen)
    strip.setPixelColor(3, colorgreen)
    strip.setPixelColor(4, colorgreen)
    strip.setPixelColor(5, colorgreen)
    strip.setPixelColor(6, colorgreen)
    strip.setPixelColor(7, colorgreen)
    print(spieler3 + " war am flinksten!")
    strip.show()


def player4_win():
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
    strip.setPixelColor(0, coloryellow)
    strip.setPixelColor(1, coloryellow)
    strip.setPixelColor(2, coloryellow)
    strip.setPixelColor(3, coloryellow)
    strip.setPixelColor(4, coloryellow)
    strip.setPixelColor(5, coloryellow)
    strip.setPixelColor(6, coloryellow)
    strip.setPixelColor(7, coloryellow)
    print(spieler4 + " war am flinksten!")
    strip.show()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[0;34m'
    OKGREEN = '\033[0;32m'
    WARNING = '\033[93m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# START
GPIO.output(24, GPIO.LOW)
print(bcolors.OKBLUE  + '''\n\n\n\n                                                          ┌┐┌┐┌┐┌┐┌┐┌┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┌───┐░░░░░░░░░┌┐░░░░░░░░░░┌───┐░░░░░░░░░░
                                                          ││││││││││││░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│┌─┐│░░░░░░░░┌┘└┐░░░░░░░░░│┌─┐│░░░░░░░░░░
                                                          │││││├┤│││││┌┬──┬┐┌┬┐┌┬──┬─┐░┌───┬┐┌┐┌┐┌┬─┐┌──┬──┬─┬──┬┐┌┐│└─┘├──┬──┬──┼┐┌┼┬──┬─┐░░░││░└┼──┬┐┌┬──┐░
                                                          │└┘└┘├┤││││└┘┤┌┐│└┘│└┘││─┤┌┐┐├──│││││││││┌┐┤──┤│─┤┌┤│─┤└┘││┌┐┌┤│─┤┌┐│┌─┘││├┤┌┐│┌┐┬──┤│┌─┤┌┐│└┘││─┤░
                                                          └┐┌┐┌┤│└┤└┤┌┐┤└┘││││││││─┤│││││──┤└┘││└┘│││├──││─┤│││─┤││││││└┤│─┤┌┐│└─┐│└┤│└┘│││├──┤└┴─│┌┐│││││─┼┐
                                                          ░└┘└┘└┴─┴─┴┘└┴──┴┴┴┴┴┴┴──┴┘└┘└───┴──┘└──┴┘└┴──┴──┴┘└──┴┴┴┘└┘└─┴──┴┘└┴──┘└─┴┴──┴┘└┘░░└───┴┘└┴┴┴┴──┴┘
''' + bcolors.ENDC)
print("\n\n\n\n")

# Einstellung
print(bcolors.WARNING + "\033[1mEinstellung:" + bcolors.ENDC)
anzRunden = int(input("Wie viele Runden wollen Sie spielen?  "))
print("")
spieler1 = raw_input("Spieler 1 Name:   ")
print("")
spieler2 = raw_input("Spieler 2 Name:   ")
print("")
spieler3 = raw_input("Spieler 3 Name:   ")
print("")
spieler4 = raw_input("Spieler 4 Name:   ")
print("")
print(bcolors.BOLD + "\n                                                                  \033[94mHerzlich Willkommen " + spieler1 + ", " + spieler2 + ", " + spieler3 + " und " + spieler4 + " zu unserem Reaction-Game!" + bcolors.ENDC)
print("")
print(bcolors.WARNING + "\033[1mINFO:" + bcolors.ENDC)
print(bcolors.WARNING + "Als erstes ändert sich der LED-STRIP viermal, danach kommt ein Piipser der irgendwann von 1 bis 5 Sekunden runterzählt und DANN sollt Ihr so schnell wie möglich DRÜCKEN." + bcolors.ENDC)
print("")
print(bcolors.WARNING + "Drücke Sie den " + bcolors.ENDC + "\033[1mWEISSEN KNOPF\033[0m" + bcolors.WARNING +" um das Spiel zu STARTEN!" + bcolors.ENDC)


# Spiel
for runde in range(anzRunden):

    while True:
        if startbutton.is_pressed:
            animation()
            break
        time.sleep(0.1)

    sleepCount = randint(1, 5)
    sleep(sleepCount)


    time.time()
    # Beep
    GPIO.output(24, GPIO.HIGH)
    start = time.time()

    # Game-Loop
    while True:

        if player1.is_pressed:
            end = time.time()
            player1_win()
            break

        if player2.is_pressed:
            end = time.time()
            player2_win()
            break

        if player3.is_pressed:
            end = time.time()
            player3_win()
            break

        if player4.is_pressed:
            end = time.time()
            player4_win()
            break

        time.sleep(0.01)


    print("Du hast {}s gebraucht!".format(round(end-start, 2)))
    print("Die echte Zeit ist: {}s".format(end-start))
    if anzRunden > 1:
        print(bcolors.WARNING + "Drücke Sie den " + bcolors.ENDC + "\033[1mWEISSEN KNOPF\033[0m" + bcolors.WARNING +" nochmal um das Spiel zu STARTEN!" + bcolors.ENDC)
    elif anzRunden < 1:
        print(bcolors.BOLD + '''\n\n                                                                                     \033[0;31m╔═══╗░░░░░░░░░╔═══╗░░░░░░░╔╗
                                                                                     ║╔═╗║░░░░░░░░░║╔═╗║░░░░░░░║║
                                                                                     ║║░╚╬══╦╗╔╦══╗║║░║╠╗╔╦══╦═╣║
                                                                                     ║║╔═╣╔╗║╚╝║║═╣║║░║║╚╝║║═╣╔╩╝
                                                                                     ║╚╩═║╔╗║║║║║═╣║╚═╝╠╗╔╣║═╣║╔╗
                                                                                     ╚═══╩╝╚╩╩╩╩══╝╚═══╝╚╝╚══╩╝╚╝
''' + bcolors.ENDC)
        break
