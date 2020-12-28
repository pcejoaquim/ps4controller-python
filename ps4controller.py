import pygame
import json 
import time

class ps4controller(object):

    def __init__(self):
        pygame.init()
        self._debug=False
        self.DZ = .4 #Analog Stick Dead Zone
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
        for joystick in self.joysticks:
            joystick.init()

        self.button_keys = {     "x": 0,
                            "circle": 1,
                            "square": 2,
                            "triangle": 3,
                            "share": 4,
                            "PS": 5,
                            "options": 6,
                            "left_stick_click": 7,
                            "right_stick_click": 8,
                            "L1": 9,
                            "R1": 10,
                            "up_arrow": 11,
                            "down_arrow": 12,
                            "left_arrow": 13,
                            "right_arrow": 14,
                            "touchpad": 15
                            }                       
        # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
        # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
        self.analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
    
    @property
    def debug(self):
        print (f'Debug status:  {self._debug}')
        return self._debug

    @debug.setter
    def debug(self, enable=False):
        if enable == True: 
            self._debug = True
        else:
            self._debug = False

    def debug_msg(self,message):
        if self._debug:
            print('Debug: ',message)
        
    def read_event(self):
        events = pygame.event.get()
        keyspressed = {}
        for event in events:
            try:
                key = self.get_key(event)
                if key != None: 
                    keyspressed.update(key)
            except:
                pass
        if keyspressed != {}:    self.debug_msg(keyspressed)
        

    def get_key(self,event):
        buttons = {}
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYDOWN:
            pass

        #Buttons
        if event.type == pygame.JOYBUTTONDOWN:
            self.debug_msg(f'Button code {event.button} is ON')
  
            if event.button == self.button_keys['left_arrow']:
                buttons['left_arrow']=100
            if event.button == self.button_keys['right_arrow']:
                buttons['righ_arrow']=100
            if event.button == self.button_keys['down_arrow']:
                buttons['down_arrow']=100
            if event.button == self.button_keys['up_arrow']:
                buttons['up_arrow']=100
            if event.button == self.button_keys['x']:
                buttons['x']=100
            if event.button == self.button_keys['circle']:
                buttons['circle']=100
            if event.button == self.button_keys['square']:
                buttons['square']=100
            if event.button == self.button_keys['triangle']:
                buttons['triangle']=100
            if event.button == self.button_keys['L1']:
                buttons['L1']=100
            if event.button == self.button_keys['R1']:
                buttons['R1']=100
            if event.button == self.button_keys['PS']:
                buttons['PS']=100
            if event.button == self.button_keys['share']:
                buttons['share']=100 
            if event.button == self.button_keys['options']:
                buttons['options']=100 
                            
        if event.type == pygame.JOYBUTTONUP:
            self.debug_msg(f'Button Code {event.button} is OFF')
  
            if event.button == self.button_keys['left_arrow']:
                buttons['left_arrow']=0                
            if event.button == self.button_keys['right_arrow']:
                 buttons['righ_arrow']=0
            if event.button == self.button_keys['down_arrow']:
                buttons['down_arrow']=0
            if event.button == self.button_keys['up_arrow']:
                buttons['up_arrow']=0
            if event.button == self.button_keys['x']:
                buttons['x']=0
            if event.button == self.button_keys['circle']:
                buttons['circle']=0
            if event.button == self.button_keys['square']:
                buttons['square']=0
            if event.button == self.button_keys['triangle']:
                buttons['triangle']=0
            if event.button == self.button_keys['L1']:
                buttons['L1']=0
            if event.button == self.button_keys['R1']:
                buttons['R1']=0
            if event.button == self.button_keys['PS']:
                buttons['PS']=0
            if event.button == self.button_keys['share']:
                buttons['share']=0 
            if event.button == self.button_keys['options']:
                buttons['options']=0 
       
        # Analog Inputs 
        if event.type == pygame.JOYAXISMOTION:

            self.analog_keys[event.axis] = event.value
            if abs(self.analog_keys[0]) > self.DZ:
                if self.analog_keys[0] < -self.DZ:
                    buttons['analogH1']=(round(self.analog_keys[0]*100))
                if self.analog_keys[0] > self.DZ:
                    buttons['analogH1']=round(self.analog_keys[0]*100)
                
            # Vertical Analog 1 
            if abs(self.analog_keys[1]) > self.DZ:
                if self.analog_keys[1] < -self.DZ:
                    buttons['analogV1']=(round(self.analog_keys[1]*100))
                if self.analog_keys[1] > self.DZ:
                    buttons['analogV1']=round(self.analog_keys[1]*100)
              
            
            # Horizontal Analog 2
            if abs(self.analog_keys[2]) > self.DZ:
                if self.analog_keys[2] < -self.DZ:
                    buttons['analogH2']=(round(self.analog_keys[2]*100))
                if self.analog_keys[2] > self.DZ:
                    buttons['analogH2']=round(self.analog_keys[2]*100)
                
            # Vertical Analog 2
            if abs(self.analog_keys[3]) > self.DZ:
                if self.analog_keys[3] < -self.DZ:
                    buttons['analogV2']=(round(self.analog_keys[3]*100))
                if self.analog_keys[3] > self.DZ:
                    buttons['analogV2']=round(self.analog_keys[3]*100)
            
            if self.analog_keys[4] > -self.DZ:  
                buttons['triggerL']=(round(((self.analog_keys[4]+1)/2)*100))
            if self.analog_keys[5] > -self.DZ:  
                buttons['triggerR']=(round(((self.analog_keys[5]+1)/2)*100))

        if buttons != {}: return(buttons)
         


if __name__ == "__main__":
    joystick=ps4controller()
    joystick.debug=True
    while True :
        joystick.read_event()
        time.sleep(0.1)
    pass