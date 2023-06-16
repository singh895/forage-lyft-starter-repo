from abc import ABC, abstractmethod


class Model():
    
    @abstractmethod
    def needs_service(self):
        pass
