from layouts.layouts.abs_layout import Layout

def supports_layouts(cls : type):
    '''Unwraps the values of the layouts in the props'''
    def get_layout(self, item):
        if isinstance(self[item], Layout): return object.__getattribute__(self, item).value
        return object.__getattribute__(self, item)
    
    cls.__getattribute__ = get_layout