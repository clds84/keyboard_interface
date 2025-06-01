#import KMK modules
from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC

#window zoom out
MINUS_ZOOM = simple_key_sequence(
        (
            KC.LCMD(no_release=True),
            KC.MACRO_SLEEP_MS(30),
            KC.MINUS,
            KC.MACRO_SLEEP_MS(30),
            KC.L(no_press=True),
        )
)
#window zoom in
PLUS_ZOOM = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.PLUS,
        KC.MACRO_SLEEP_MS(30),
        KC.LCMD(no_press=True),
    )
)
#window zoom default (100%)
DEFAULT_ZOOM = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.N0,
        KC.MACRO_SLEEP_MS(30),
        KC.LCMD(no_press=True),
    )
)
#scroll tabs right
TABS_RIGHT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LALT(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.RIGHT,
        KC.MACRO_SLEEP_MS(30),
    )
)
#scroll tabs left
TABS_LEFT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LALT(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.LEFT,
        KC.MACRO_SLEEP_MS(30),
    )
)
#close tab
TABS_CLOSE = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.W,
    )
)
#highlight by word left of cursor
HIGHLIGHT_WORD_LEFT = simple_key_sequence(
    (
        KC.LALT(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.LEFT
    )
)
#highlight by word right of cursor
HIGHLIGHT_WORD_RIGHT = simple_key_sequence(
    (
        KC.LALT(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.RIGHT
    )
)
#highlight by line left of cursor
HIGHLIGHT_LINE_LEFT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.LEFT
    )
)
#highlight by line right of cursor
HIGHLIGHT_LINE_RIGHT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.RIGHT
    )
)
#highlight by line left and up from cursor. First time will highlight left and then continue up - UNUSED
HIGHLIGHT_LINE_UP = simple_key_sequence(
    (
        KC.LALT(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.UP
    )
)
#highlight by line right and down from cursor. First time will highlight right and then continue down - UNUSED
HIGHLIGHT_LINE_DOWN = simple_key_sequence(
    (
        KC.LALT(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.DOWN
    )
)
#highlight by block up from cursor. First time will highlight left and then continue up - UNUSED
HIGHLIGHT_BLOCK_UP = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.UP
    )
)
#highlight by block down from cursor. First time will highlight right and then continue down - UNUSED
HIGHLIGHT_BLOCK_DOWN = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.DOWN
    )
)
#copy text
COPY = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.C,
    )
)
#cut text
CUT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.X,
    )
)
#paste text
PASTE = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.V,
    )
)
#puts cursor in address bar or highlights address bar
ADDRESS_BAR = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.L
    )
)
#toggle Zoom video
ZOOM_VIDEO = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.V
    )
)
#toggle Zoom audio
ZOOM_AUDIO = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.A
    )
)
#toggle Zoom screenshare
ZOOM_SCREEN_SHARE = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.S
    )
)
#Exit Zoom (will be prompted to confirm). Note: this is a pretty standard keyboard shortcut.
#It closes tabs as well, but for the purpose of this project, the encoder designated for tab functionality
#is not in the layer that includes Zoom shortcuts.
ZOOM_CLOSE = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.W
    )
)
#toggle Zoom gallery view
ZOOM_GALLERY_VIEW = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.W
    )
)
#Zoom next gallery
ZOOM_GALLERY_NEXT = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.N
    )
)
#Zoom previous gallery
ZOOM_GALLERY_PREVIOUS = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.P
    )
)
#Zoom open participant panel
ZOOM_PARTICIPANT_PANEL = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.U
    )
)
#undo last action
UNDO = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.Z
    )
)
#redo last action
REDO = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.LSHIFT(no_release=True),
        KC.Z
    )
)
#go back to previous page
CHROME_BACK = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.LEFT
    )
)
#go forward page
CHROME_FOWARD = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.RIGHT
    )
)
#start Google Slides slideshow
SLIDESHOW = simple_key_sequence(
    (
        KC.LCMD(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.ENTER
    )
)
#scroll browser page slower than page up/down. KC.UP called twice so it's not 
#as slow as one
UP = simple_key_sequence(
    (
        KC.UP,
        KC.MACRO_SLEEP_MS(30),
        KC.UP
    )
)
#scroll browser page slower than page up/down. KC.DOWN called twice so it's not 
#as slow as one
DOWN = simple_key_sequence(
    (
        KC.DOWN,
        KC.MACRO_SLEEP_MS(30),
        KC.DOWN
    )
)
#press to copy, hold to cut
CUT_COPY = KC.HT(COPY, CUT)
