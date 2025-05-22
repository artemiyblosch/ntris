from abc import ABC, abstractmethod
from layouts.observers.Observer import Observer

class Layout(ABC):
    @abstractmethod
    @property
    def observer() -> Observer:
        pass
    
    @abstractmethod
    def update(self):
        pass

    def subscribe(self):
        self.observer.add(self)

    def unsubscribe(self):
        self.observer.remove(self)