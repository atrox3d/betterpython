from abc import ABC, abstractmethod


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):
    authorized: bool = False

    def verify_code(self, code):
        print(f'Verifying code {code}')
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized

class NotARobot(Authorizer):
    authorized: bool = False

    def not_a_robot(self):
        print('are you a robot? n')
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized

