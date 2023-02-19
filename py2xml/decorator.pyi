from .element import Element
import typing as t

P = t.ParamSpec('P')

@t.overload
def to_element(func: t.Callable[P, None]) -> Element[P]: ...
_to_element = to_element

@t.overload
def to_element(*, name: str) -> t.Callable[[t.Callable[P, None], Element[P]]]: ...