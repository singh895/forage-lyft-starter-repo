from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for t in self.tire_wear:
            if t>=0.9:
                return True
        return False


