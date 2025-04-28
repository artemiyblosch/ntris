def avg(lst : list):
    return sum(lst)/len(lst)

def enum(map):
    ret = []
    for x in map.map:
        for y in map.map[x]:
            ret.append([(x,y),map[x,y]])
    return ret

def rotate(p : tuple[int,int], a : tuple[int,int]) -> tuple[int,int]:
  return (-p[1]+a[1]+a[0],p[0]-a[0]+a[1])

def flip(p : tuple[int,int], a : int) -> tuple[int,int]:
    return (2*a-p[0],p[1])

def filterD(d):
    return dict(filter(lambda item: item[1] != None, d.items()))

def has(l,v):
    return bool(sum([1 for i in l if i == v]))

class ModeLink:
    def __init__(self,mode):
        self.mode = mode
    
    def set_mode(self,mode):
        self.mode = mode