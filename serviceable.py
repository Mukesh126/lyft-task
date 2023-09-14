from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        """Determine if the object needs service."""
        pass
