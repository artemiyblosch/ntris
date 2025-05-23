from layouts.layouts.abs_layout import Layout

def supports_layouts(cls : type):
    '''Unwraps the values of the layouts in the props'''
    def get_layout(self, item):
        attr = object.__getattribute__(self, item)

        if isinstance(attr, Layout): return attr.value
        if isinstance(attr, tuple) and list(map(type, attr))[1] == tuple:
            grid,pos = attr
            return grid[pos]
        
        return attr
    
    cls.__getattribute__ = get_layout
    return cls