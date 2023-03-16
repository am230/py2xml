from .element import Element
import typing as t

P = t.ParamSpec('P')

def to_element(func: t.Callable[P, None]=None, name: t.Optional[str]=None):
    def wrapper(func: t.Callable[P, None]) -> Element[P]:
        return Element.from_name(name or func.__name__, attrs=func)

    if func is None:
        return wrapper
    
    return wrapper(func)