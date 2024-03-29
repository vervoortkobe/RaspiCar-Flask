from domain.car import Car

class Raspberry_service:
    def __init__(self):
        self.car = Car()
    
        self.forward_pressed = False
        self.backward_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        
    def press_forward(self):
        self.forward_pressed = True
        
        # check forward / backward
        if self.forward_pressed:
            self.car.drive_forward()
        if self.forward_pressed and self.backward_pressed:
            self.car.stop_driving()
            
        # check left / right
        if self.left_pressed:
            self.car.turn_left()
        elif self.right_pressed:
            self.car.turn_right()
    
        
    def release_forward(self):
        self.forward_pressed = False
        
        # check forward / backward
        if self.backward_pressed:
            self.car.drive_backward()
        else:
            self.car.stop_driving()
            
        # check left / right
        if self.left_pressed:
            self.car.turn_left()
        if self.right_pressed:
            self.car.turn_right()
        
    def press_backward(self):
        self.backward_pressed = True
        
        # check forward / backward
        if self.backward_pressed:
            self.car.drive_backward()
        if self.forward_pressed and self.backward_pressed:
            self.car.stop_driving()
            
        # check left / right
        if self.left_pressed:
            self.car.turn_left()
        elif self.right_pressed:
            self.car.turn_right()
    
        
    def release_backward(self):
        self.backward_pressed = False
        
        # check forward / backward
        if self.forward_pressed:
            self.car.drive_forward()
        else:
            self.car.stop_driving()
            
        # check left / right
        if self.left_pressed:
            self.car.turn_left()
        elif self.right_pressed:
            self.car.turn_right()
            
    def press_right(self):
        self.right_pressed = True
        self.car.turn_right()
        
    def release_right(self):
        self.right_pressed = False
        self.car.stop_driving()
        
        if self.backward_pressed:
            self.car.drive_backward()
        elif self.forward_pressed:
            self.car.drive_forward()
            
    def press_left(self):
        self.left_pressed = True
        self.car.turn_left()
        
    def release_left(self):
        self.left_pressed = False
        self.car.stop_driving()
        
        if self.backward_pressed:
            self.car.drive_backward()
        elif self.forward_pressed:
            self.car.drive_forward()
    