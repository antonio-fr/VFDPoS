  VFDPoS
===========

VFDPoS is a Python library dedicated for driving Wincor Nixdorf Point of Sale VFD USB, such as BA-66 USB. This library should be compatible with any WN BA-6x USB VFD.

Provides high level abstraction to use Wincor Nixdorf Point of Sale VFD USB

* Easy to use and handle, play with your VFD in no time
* Cross-platform code and dependencies
* Full python code to access VFD through USB
* Character encoding automatic conversion
* limited python dependencies (some provided in zip)


## Dependencies

This library needs PyUSB, it can work on mutiple OS platform.
PyUSB always requires libusb.

You only need libusb if you download the release zip file VFDPOS_vxx.zip.

Some examples which pull info from Internet require Easy-REST-JSON library available at 
https://github.com/antonio-fr/Easy-REST-JSON

To test quickly, copy examples at the same level as the library (vfdpos.py) and run them.

## Using library

### Linux

You need to install libusb-1.0 and PyUSB. PyUSB is provided in the zip release.

For example in Ubuntu 14 :

    sudo apt-get install python libusb-1.0-0-dev
    git clone https://github.com/walac/pyusb
    cd pyusb && sudo python setup.py install


### Windows

In windows you can use instead of this library : VFD-POS, which is very similar but provides driver-less, null installation and platform specific access to VFD.
https://github.com/antonio-fr/VFD-POS


If you need universal and cross-platform Python code, you can still use this library. On Windows, this requires libusb-win32 driver installed and loaded for the WN VFD.
The easiest way is to get Zadig and to select libusb-win32 for the Diplay Interface of your WN VFD.
http://zadig.akeo.ie/ Then you need PyUSB (provided in zip release).




### Use Library

To use the library, just copy vfdpos.py and use import as 

usual

    import vfdpos

or

    from vfdpos import *


#### Initialisation

Class constructor detects, tries to connect to VFD, initializes it and finally returns a library object to send commands. You need USB product ID (PID) of the VFD. For BA66 USB, this is 0x0201. For some others models this can be 0x0200.

    MyVFD = vfdpos.vfd_pos(PRODUCT_ID)


#### Self-Test

Tell the VFD to perform self-test. You may need to initialize VFD again after do so.

    MyVFD.selftest()


#### Reset

Tell the VFD to perform a reboot. You need to initialize VFD again after do so.

    MyVFD.reset()


#### Set Charset

Set the VFD charset. See your WN operational manual documentation for char code.
During initilisation, WN VFD is automatically set up to 0x31 = Code Page 858. Don't change it unless you really have specific need, this would cause issues with write_msg function.

Character tables are available in :
https://www.dieboldnixdorf.com/-/media/diebold/ag-downloads/poslotterysystems/manuals/peripherals/baxx/ba63_character_appendix_german.pdf

    MyVFD.set_charset(CHARSET_CODE)


#### Clear Screen

Clear and erase the VFD screen.

    MyVFD.clearscreen()


#### Print Character

Print a character from its number at the cursor position

    MyVFD.printchr(CHAR_CODE)


#### Position Cursor

Change the position of the cursor to a given column and line. If 0 is provided for a parameter, no change is performed for it.

    MyVFD.poscur(LINE, COLUMN)


#### Write Message

Write a message to the VFD screen at the cursor position. This function uses automatic decoding of any unicode character. In case you provide direclty the string don't forget trailing u (  u"string" ). If you change the charset to another one, this function might bring some issues. You can use "\r" and "\n" inside the string to get line control.

    MyVFD.write_msg(MESSAGE_STRING)


#### Close Device

When python program stops, the display keep lighting. This command clears the display. Useful if you need to light off the VFD after using it.

    MyVFD.close()


**Form more details: see code in examples directory**


## Example :
The following example displays a basic text on a BA66 USB VFD.

    import vfdpos
    wnpos = vfdpos.vfd_pos(0x0201)
    wnpos.write_msg("Hello World !\r\nThat works :)")
    raw_input("PRESS ENTER TO EXIT")


Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
