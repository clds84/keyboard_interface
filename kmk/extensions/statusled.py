# Use this extension for showing layer status with three leds

import pwmio
import time
import busio
import board

from kmk.extensions import Extension, InvalidExtensionEnvironment
from kmk.keys import make_key
from kmk.utils import Debug

debug = Debug(__name__)

import displayio, terminalio
import adafruit_displayio_ssd1306

#For 128x128 display
# import adafruit_ssd1327 (128x128)

from adafruit_display_text import label

displayio.release_displays()

i2c = busio.I2C(board.GP3, board.GP2)

# For ssd1327(128x64) display
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

#####################################For 128x128 display#####################################
#display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
#display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)

# color_bitmap = displayio.Bitmap(128, 64, 1)
# color_palette = displayio.Palette(1)
# color_bitmap = displayio.Bitmap(128, 64, 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0x000000  # Whitecolor_palette[0] = 0x000000  # White

# font_file = "fonts/LeagueSpartan-Bold-16.bdf"


class statusLED(Extension):
    def __init__(
        self,
        led_pins,
        brightness=30,
        brightness_step=5,
        brightness_limit=100,
    ):
        self._leds = []
        for led in led_pins:
            try:
                self._leds.append(pwmio.PWMOut(led))
            except Exception as e:
                print(e)
                raise InvalidExtensionEnvironment(
                    'Unable to create pulseio.PWMOut() instance with provided led_pin'
                )
        self._led_count = len(self._leds)

        self.brightness = brightness
        self._layer_last = -1

        self.brightness_step = brightness_step
        self.brightness_limit = brightness_limit

        make_key(names=('SLED_INC',), on_press=self._key_led_inc)
        make_key(names=('SLED_DEC',), on_press=self._key_led_dec)

    def _layer_indicator(self, layer_active, *args, **kwargs):
        '''
        Indicates layer with LEDs and updates the display
        '''

        if self._layer_last != layer_active:
            led_last = 0 if self._layer_last == 0 else 1 + (self._layer_last - 1) % 3
            led_active = 0 if layer_active == 0 else 1 + (layer_active - 1) % 3

            self.set_brightness(0, led_last)
            self.set_brightness(self.brightness, led_active)

            # Set up display
            display.root_group = None
            splash = displayio.Group()
            display.root_group = splash
            display.show(splash)

            # Layer-specific label data
            label_sets = {
                0: [
                    ("UNDO", 5, 50), ("REDO", 60, 50),
                    ("CUT/COPY", 5, 60), ("PASTE", 60, 60),
                    ("TAB", 110, 4), ("COMMAND", 87, 15),
                    ("HL W", 105, 54), ("<CHROME>", 20, 38),
                    ("", 0, 32, 2), ("PAGE U/D", 81, 26),
                    ("TABS", 105, 38), ("R/L", 35, 26),
                ],
                1: [
                    ("UNDO", 5, 50), ("REDO", 60, 50),
                    ("CUT/COPY", 5, 60), ("PASTE", 60, 60),
                    ("TAB", 110, 4), ("COMMAND", 87, 15),
                    ("HL L", 105, 54), ("<CHROME>", 20, 38),
                    ("", 0, 32, 2), ("ARROW U/D", 75, 26),
                    ("TABS", 105, 38), ("R/L", 35, 26),
                ],
                2: [
                    ("ESCAPE", 5, 50), ("ENTER", 60, 50),
                    ("SHARE", 5, 60), ("END", 60, 60),
                    ("ZOOM AUDIO", 68, 4), ("ZOOM VIDEO", 68, 15),
                    ("HL W", 105, 54), ("AUDIO", 20, 26),
                    ("", 0, 32, 2), ("SLIDESHOW", 74, 26),
                    ("GALLERY", 105, 38),
                ],
            }

            labels = []
            for item in label_sets.get(layer_active, []):
                text, x, y = item[0], item[1], item[2]
                scale = item[3] if len(item) > 3 else 1
                labels.append(label.Label(terminalio.FONT, text=text, scale=scale, color=0xFFFF00, x=x, y=y))

            for lbl in labels:
                splash.append(lbl)

            self._layer_last = layer_active


    def __repr__(self):
        return f'SLED({self._to_dict()})'

    def _to_dict(self):
        return {
            'brightness': self.brightness,
            'brightness_step': self.brightness_step,
            'brightness_limit': self.brightness_limit,
        }

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        '''Light up every single led once for 200 ms'''
        for i in range(self._led_count + 2):
            if i < self._led_count:
                self._leds[i].duty_cycle = int(self.brightness / 100 * 65535)
            i_off = i - 2
            if i_off >= 0 and i_off < self._led_count:
                self._leds[i_off].duty_cycle = int(0)
            time.sleep(0.1)
        for led in self._leds:
            led.duty_cycle = int(0)
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        self._layer_indicator(sandbox.active_layers[0])
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        self.set_brightness(0)
        return

    def on_powersave_disable(self, sandbox):
        self.set_brightness(self.brightness)
        self._leds[2].duty_cycle = int(50 / 100 * 65535)
        time.sleep(0.2)
        self._leds[2].duty_cycle = int(0)
        return

    def set_brightness(self, percent, layer_id=-1):
        if layer_id < 0:
            for led in self._leds:
                led.duty_cycle = int(percent / 100 * 65535)
        else:
            self._leds[layer_id - 1].duty_cycle = int(percent / 100 * 65535)

    def increase_brightness(self, step=None):
        if not step:
            self.brightness += self.brightness_step
        else:
            self.brightness += step

        if self.brightness > 100:
            self.brightness = 100

        self.set_brightness(self.brightness, self._layer_last)

    def decrease_brightness(self, step=None):
        if not step:
            self.brightness -= self.brightness_step
        else:
            self.brightness -= step

        if self.brightness < 0:
            self.brightness = 0

        self.set_brightness(self.brightness, self._layer_last)

    def _key_led_inc(self, *args, **kwargs):
        self.increase_brightness()

    def _key_led_dec(self, *args, **kwargs):
        self.decrease_brightness()
