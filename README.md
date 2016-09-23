#ducky2arduino
convert rubber ducky payloads into arduino sketches using a simple python script.

##How to use:
Just put a payload named input.txt in the same folder as the script and run it.
You will get an output.ino file wich can be opened in the Arduino IDE directly to upload it to an Arduino/Genuino Leonardo or Micro.

##Please note:
that PRINTSCREEN, SCROLLLOCK and NUMLOCK are not supported yet.

You may carefully read the rubber ducky syntax before converting.
  https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript

If you want to combine keys make sure to write SHIFT, ALT, CTRL and GUI first because because there are no more statements considered after arrow keys, CAPSLOCK, DELETE, END, ESC or ESCAPE, HOME, INSERT, NUMLOCK, PAGEUP, PAGEDOWN, SPACE or TAB.

##Thank you in advance for sharing and reporting issues or suggestions to improve this script.
