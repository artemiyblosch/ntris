class Timer:
    def __init__(self, amount : int = 1, framerate : int = 1):
        self.delay = amount/framerate
        self.__counter = 0
    
    def tick(self,framerate : int = 60) -> bool:
        self.__counter += 1/framerate
        if self.__counter > self.delay: self.__counter = 0
        return self.__counter == 0