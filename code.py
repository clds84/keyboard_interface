print("Starting")

#Import macros (key_sequence)
import key_sequence

#Import GPIO pin assignments
import board

#Import KMK core and modules
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.statusled import statusLED
from kmk.modules.holdtap import HoldTap

#Instantiate KMK, layers, encoders, and HoldTap
keyboard = KMKKeyboard()
layers = Layers()
encoder1 = EncoderHandler()
encoder2 = EncoderHandler()
encoder3 = EncoderHandler()
encoder4 = EncoderHandler()
encoder5 = EncoderHandler()
encoder6 = EncoderHandler()

#Instantiate for multipurpose key
#Example: press to copy and hold to cut
#See key_sequences.py
holdtap = HoldTap()

#Register instances
keyboard.modules = [
        layers,
        encoder1,
        encoder2,
        encoder3,
        encoder4,
        encoder5,
        encoder6,
        holdtap,
    ]

#Uncomment for debugging
# keyboard.debug_enabled = False 

#Setup key matrix and diode orientation
keyboard.col_pins = (board.GP27,board.GP28,)
keyboard.row_pins = (board.GP22,board.GP26,board.GP21,board.GP20)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

#Setup pin orientation for encoders for turning clockwise, counter-clockwise, and switch press)
encoder1.pins = ((board.GP18, board.GP17, board.GP16, False),)
encoder2.pins = ((board.GP12, board.GP11, board.GP10, False),)
encoder3.pins = ((board.GP9, board.GP8, board.GP7, False),)
encoder4.pins = ((board.GP15, board.GP14, board.GP13, False),)
encoder5.pins = ((board.GP6, board.GP5, board.GP4, False),)

#LEDs indicate current active layer. Only one is on at a time
status_led = statusLED(
    led_pins=[board.GP1, board.GP19, board.GP0],
    brightness=30,
    brightness_step=5,
    brightness_limit=100,
    )

keyboard.extensions.append(status_led)

#Define layers
LAYER_1, LAYER_2, LAYER_3  = 0, 1, 2

#Define keys to switch between layers
TO_LAYER_1 = KC.TO(LAYER_1)
TO_LAYER_2 = KC.TO(LAYER_2)
TO_LAYER_3 = KC.TO(LAYER_3)

#Press to copy, hold to cut
CUT_COPY = KC.HT(key_sequence.COPY, key_sequence.CUT)

# Keymap for 4 bottom white keys, 2 top white keys, and a black layer-switch key
keyboard.keymap = [
    [
        key_sequence.UNDO, key_sequence.REDO,
        CUT_COPY, key_sequence.PASTE,
        key_sequence.KC.LCMD, key_sequence.KC.TAB,
        TO_LAYER_2
    ],
    [
        key_sequence.UNDO, key_sequence.REDO,
        CUT_COPY, key_sequence.PASTE,
        key_sequence.KC.LCMD, key_sequence.KC.TAB,
        TO_LAYER_3,
    ],
    [
        key_sequence.KC.ESCAPE, key_sequence.KC.ENTER,
        key_sequence.ZOOM_SCREEN_SHARE, key_sequence.ZOOM_CLOSE,
        key_sequence.ZOOM_VIDEO, key_sequence.ZOOM_AUDIO,
        TO_LAYER_1,
    ],
]

#layer map for encoders

#bottom right encoder
encoder1.map = [
                ((key_sequence.HIGHLIGHT_WORD_LEFT, key_sequence.HIGHLIGHT_WORD_RIGHT,TO_LAYER_2),), #LAYER_1
                ((key_sequence.HIGHLIGHT_LINE_LEFT,key_sequence.HIGHLIGHT_LINE_RIGHT,TO_LAYER_1),), #LAYER_2
                ((KC.NO,KC.NO,KC.NO),), #LAYER_3, KC.NO = no operation
]
#bottom left encoder
encoder2.map = [
                ((key_sequence.CHROME_BACK, key_sequence.CHROME_FOWARD,key_sequence.ADDRESS_BAR),), #LAYER_1
                ((key_sequence.CHROME_BACK, key_sequence.CHROME_FOWARD,key_sequence.ADDRESS_BAR),), #LAYER_2
                ((KC.NO,KC.NO,KC.NO),), #LAYER_3
]
#top left encoder
encoder3.map = [
                ((KC.LEFT,KC.RIGHT,KC.F14),), #LAYER_1
                ((KC.LEFT,KC.RIGHT,KC.F14),), #LAYER_2
                ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE),), #LAYER_3
]
#middle right encoder
encoder4.map = [
                ((key_sequence.TABS_LEFT, key_sequence.TABS_RIGHT, key_sequence.TABS_CLOSE),),#LAYER_1
                ((key_sequence.TABS_LEFT, key_sequence.TABS_RIGHT, key_sequence.TABS_CLOSE),),#LAYER_2
                ((key_sequence.ZOOM_GALLERY_PREVIOUS, key_sequence.ZOOM_GALLERY_NEXT, key_sequence.ZOOM_GALLERY_VIEW),), #LAYER_3
]
#top right encoder
encoder5.map = [
                ((KC.PGUP, KC.PGDOWN, KC.HOME),), #LAYER_1
                ((key_sequence.UP, key_sequence.DOWN, KC.HOME),), #LAYER_2
                ((KC.UP,KC.DOWN, key_sequence.SLIDESHOW),), #LAYER_3
]

if __name__ == '__main__':
    keyboard.go()


