import typing as t
import types_ as tp
from mapgen import Map

def avg(lst : list[int]):
    return sum(lst)/len(lst)

def enum(map : Map) -> list[list]:
    ret = []
    for x in map.map:
        for y in map.map[x]:
            ret.append([(x,y),map[x,y]])
    return ret

def rotate(p : tp.Point, a : tp.Point) -> tp.Point:
  return (-p[1]+a[1]+a[0],p[0]-a[0]+a[1])

def flip(p : tp.Point, a : int) -> tp.Point:
    return (2*a-p[0],p[1])

def filterD(d : dict):
    return dict(filter(lambda item: item[1] != None, d.items()))

G = t.TypeVar('G')
def has(l : list[G], v : G):
    return bool(sum([1 for i in l if i == v]))

def closest(arr : list[int], num : int) -> int:
    return min([(abs(i-num),i) for i in arr], key=lambda a: a[0])[1]