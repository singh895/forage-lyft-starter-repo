from abc import ABC, abstractmethod
from battery.battery import Battery
from ops import add_years_to_date

class Nubbin_Battery(Battery):
    def __init__(self, last_service_date, current_date)->None:
        #super().__init__(last_service_date, current_date)
        super(Nubbin_Battery, self).__init__(last_service_date,current_date)
    
    @abstractmethod
    def needs_service(self):
        date_for_service = add_years_to_date(self.last_service_date, 4)
        if date_for_service < self.current_date:
            return True
        else:
            return False
        
