
[![Available_in](https://img.shields.io/badge/-Available%20in-555)]()
[![Termux](https://img.shields.io/badge/-TERMUX-blue)](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US)
[![Linux](https://img.shields.io/badge/-LINUX-blue)](https://ubuntu.com/)
[![Linux](https://img.shields.io/badge/-WINDOWS-blue)](https://www.microsoft.com/en-us/windows)



[![Requirements](https://img.shields.io/badge/Requirements-Python3%20or%20Python2-blue)]()


# ducky2arduino
convert rubber ducky payloads into arduino sketches using a simple python script without coments and unused Enters.

## How to use:
clone it to your device

    git clone https://github.com/BesoBerlin/ducky2arduino

run the script and then enter your file path or name

    python3 ducky2arduino/ducky2arduino.py

You will get an output.ino file wich can be opened in the Arduino IDE directly to upload it to an Arduino/Genuino Leonardo or Micro.

## Please note:
that PRINTSCREEN, SCROLLLOCK and NUMLOCK are not supported yet.

You may carefully read the rubber ducky syntax before converting.
  https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript

If you want to combine keys make sure to write SHIFT, ALT, CTRL and GUI first because because there are no more statements considered after arrow keys, CAPSLOCK, DELETE, END, ESC or ESCAPE, HOME, INSERT, NUMLOCK, PAGEUP, PAGEDOWN, SPACE or TAB.

## Thank you in advance for sharing and reporting issues or suggestions to improve this script.
