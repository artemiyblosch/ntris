import typing as t
T = t.TypeVar('T')
class Link(t.Generic[T]):
    def __init__(self, ref : T):
        self.ref = ref
    
    def set_ref(self,ref : T):
        self.ref = ref