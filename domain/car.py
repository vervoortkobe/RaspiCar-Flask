from gpiozero import OutputDevice

class Wheel:
    def __init__(self, pin_number_1, pin_number_2):
        self.pin1 = OutputDevice(pin_number_1)
        self.pin2 = OutputDevice(pin_number_2)
        
    def stop(self):
        self.pin1.off()
        self.pin2.off()
        
    def go_forwards(self):
        self.stop()
        self.pin1.on()
        
    def go_backwards(self):
        self.stop()
        self.pin2.on()

class Car:
    def __init__(self):
        self.left_wheel = Wheel(24, 23)
        self.right_wheel = Wheel(27, 22)
        
    def stop_driving(self):
        self.left_wheel.stop()
        self.right_wheel.stop()
        
    def drive_forward(self):
        self.stop_driving()
        self.right_wheel.go_forwards()
        self.left_wheel.go_forwards()
        
    def drive_backward(self):
        self.stop_driving()
        self.right_wheel.go_backwards()
        self.left_wheel.go_backwards()
        
    def turn_right(self):
        self.stop_driving()
        self.right_wheel.go_forwards()
        self.left_wheel.go_backwards()
        
    def turn_left(self):
        self.stop_driving()
        self.right_wheel.go_backwards()
        self.left_wheel.go_forwards()
