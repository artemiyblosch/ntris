from abc import ABC, abstractmethod
from layouts.observers.Observer import Observer

meta_observer = Observer()

class Layout(ABC):
    @abstractmethod
    @property
    def observer() -> Observer:
        pass
    
    @abstractmethod
    def update(self):
        '''Updates the value of layout'''
        pass

    def subscribe(self):
        '''Subscribes self to the observer'''
        self.observer.add(self)

    def unsubscribe(self):
        '''Unsubscribes self to the observer'''
        self.observer.remove(self)