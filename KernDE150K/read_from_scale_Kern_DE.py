from __future__ import print_function
import serial
import time

# note: 
# find the usb port to use with (in terminal):
# dmesg | grep tty
# and take the last line.
# ls /dev/tty* | grep usb
# is also a possibility
usb_port_name = '/dev/ttyUSB0'

# note:
# one must set the right parameters in the scale before use!!
# follow the manual, see page 28: need to put in 'AU PC' mode to get output even if weight not constant
#                        page 29: baud rate and similar
baudrate = 18200

usb_port = serial.Serial(usb_port_name, baudrate=baudrate, timeout=0.5)
usb_port.flushInput()


def receive_one_message(start_time=None):

    list_chars = []

    crrt_char = ""

    while crrt_char != "\n":

        if usb_port.inWaiting() > 0:
            crrt_char = usb_port.read()
            list_chars.append(crrt_char)

        if crrt_char == "\n":
            crrt_string = "".join(list_chars)
            print(crrt_string)
            if start_time is not None:
                print("time_since_beginning {}".format(time.time() - start_time))


start_time = time.time()
duration_loggin_s = 2 * 60

while time.time() - start_time < duration_loggin_s:
    receive_one_message(start_time)
    
# note:
# the data can be parsed using the information from pages 32 33 34
