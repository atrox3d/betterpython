from abc import ABC, abstractmethod

class Switchable(ABC):
    """
    define Switchable interface
    """

    @abstractmethod
    def turn_on(self):
        """
        turn on device        
        """
        pass

    @abstractmethod
    def turn_off(self):
        """
        turn off device
        """
        pass


class LightBulb(Switchable):
    """
    represents a switchable lightbulb
    """

    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    """
    represents a switchable fan
    """
    
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    """
    represents an electric power switch

    turns on and off a switchable device
    """
    
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
