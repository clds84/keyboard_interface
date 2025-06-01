# Keyboard Interface (Work in Progress)

##### Hi! This project involves a Raspberry Pi Pico, key switches, rotary encoders, an OLED display, one switch, and three single LEDs. It serves as a navigation, editing, and Zoom control interface.

### Keyboard building

##### Please refer to online documentation for soldering keyboard matrices. 

### Raspberry Pi Pico

##### Please refer to Adafruit’s documentation for flashing a Pico with CircuitPython. Besides code.py and key_sequence.py, the /kmk/extensions/statusled.py file contains display-related code dependent on layer conditionals.

### KMK Firmware

##### KMK paired with a Raspberry Pi Pico is a great option for developing projects in Python. However, many keyboard enthusiasts prefer other hardware that runs QMK firmware, which is written in C. For more information about KMK firmware, the foundation of this project, please refer to the KMK repository:

##### https://github.com/KMKfw/kmk_firmware

### Layers class in KMK 

##### Layer functionality in KMK allows users to switch between different keyboard layouts. For example, you can have a standard QWERTY layout that changes to a gaming layout when a specific button is pressed. This interface includes three layers: the first two are largely similar, while the third incorporates Zoom controls. 

### Components

##### The key switches, rotary encoders, OLED display, switch, and LEDs were purchased online or at Micro Center. Select key switches according to your preference, rotary encoders that support three functions (counter-clockwise rotation, clockwise rotation, and switch press), and an OLED display, single LEDs, and a switch as linked below.

##### Note that the OLED display does not have to be the exact size included in this project, but the included .stl file is designed to fit the display linked.

### 3D Printing

##### Two .stl files are included for 3D printing the housing of the keyboard interface. One note: the micro-USB cutout is slightly (about 0.5 mm) off from the Pico’s port. This does not affect usability but can be addressed by adding a thin washer for each mounting post or by making small adjustments to the print after some testing. My priority was device functionality over perfect print fit, so please plan accordingly.

### Installation

##### While I’m not providing step-by-step installation instructions from scratch, here are some tips and lessons learned that may help if you choose to build this interface:




