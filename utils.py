import typing as t
from types_ import Point
from mapgen import Map

def avg(lst : list[int]):
    return sum(lst)/len(lst)

def enum(map : Map) -> list[list]:
    ret = []
    for x in map.map:
        for y in map.map[x]:
            ret.append([(x,y),map[x,y]])
    return ret

def rotate(p : Point, a : Point) -> Point:
  return (-p[1]+a[1]+a[0],p[0]-a[0]+a[1])

def flip(p : Point, a : int) -> Point:
    return (2*a-p[0],p[1])

def filterD(d : dict):
    return dict(filter(lambda item: item[1] != None, d.items()))

G = t.TypeVar('G')
def has(l : list[G], v : G):
    return bool(sum([1 for i in l if i == v]))

T = t.TypeVar('T')
class Link(t.Generic[T]):
    def __init__(self, ref : T):
        self.ref = ref
    
    def set_ref(self,ref : T):
        self.ref = ref

def closest(arr : list[int], num : int) -> int:
    return min([(abs(i-num),i) for i in arr], key=lambda a: a[0])[1]