from gpiozero import OutputDevice
from time import sleep

pin1 = OutputDevice(14)
pin2 = OutputDevice(15)

pin3 = OutputDevice(23)
pin4 = OutputDevice(24)

pin1.off()
pin2.off()
pin3.off()
pin4.off()
