from xml.etree import ElementTree 
import typing as t
import inspect

T = t.TypeVar('T')
P = t.ParamSpec('P')


class IElement:
    name: t.Text

    def render(self) -> str: ...


Value = t.Union[IElement, t.Text]


class Element(t.Generic[P], IElement):

    name: t.Text
    children: t.List[Value]
    attributes: t.Dict[str, t.Any]
    children_text: str

    def __init__(
        self,
        name: t.Text,
        children: t.Optional[t.List[Value]] = None,
        props: t.Optional[t.Dict[t.Text, t.Optional[t.Any]]] = None
    ) -> None:
        self.name = name
        self.children: t.List[Value] = children or []
        self.attributes = props or {}

    @classmethod
    def from_name(
        cls,
        name: str,
        *,
        attrs: t.Optional[t.Callable[P, None]] = None,
        children: t.Optional[t.List[Value]] = None,
        props: t.Optional[t.Dict[t.Text, t.Optional[t.Any]]] = None
    ) -> 'Element[P]':
        return cls(
            name=name,
            children=children,
            props=props
        )

    def copy(self) -> t.Self:
        return type(self)(
            self.name,
            self.children,
            self.attributes
        )

    def format(self, value):
        if isinstance(value, str):
            return value
        if isinstance(value, bool):
            return int(value)
        return str(value)

    def set_children(self, children: t.List[Value]) -> t.Self:
        self.children = [self.format(child) if not isinstance(child, Element) else child for child in children]
        return self

    def set_attributes(self, attributes: t.Dict) -> t.Self:
        self.attributes |= {key: self.format(value) for key, value in attributes.items()}
        return self

    def __getitem__(self, args: t.Union[t.Tuple[Value], Value]) -> t.Self:
        self = self.copy()
        if isinstance(args, tuple):
            self.set_children(list(args))
        else:
            self.set_children([args])
        return self

    def __call__(self, *args: P.args, **props: P.kwargs) -> t.Self:
        self = self.copy()
        arg_list: t.List = list(args)

        attrs = {}

        while arg_list and isinstance(arg_list[0], dict):
            attrs |= arg_list.pop(0)

        attrs |= {k: None for k in arg_list}
        attrs |= props

        self.set_attributes(attrs)

        return self
    
    def to_xml(self) -> ElementTree.Element:
        element = ElementTree.Element(self.name, attrib=self.attributes)
        element.extend(tuple(map(type(self).to_xml, (child for child in self.children if not isinstance(child, str)))))
        element.text = ''.join(child for child in self.children if isinstance(child, str))
        return element

    def render(self) -> str:
        children_text = self.children_text

        return f'<{self.name}%s>%s</{self.name}>' % (
            ' %s' % ' '.join(
                '%s="%s"' % (k, format(v)) if v is not None else k for k, v in self.attributes.items()
            ) if self.attributes else '',
            '%s' % children_text if children_text else '',
        )

    @property
    def children_text(self) -> str:
        return "".join(item.render() if isinstance(item, Element) else item for item in self.children)

    def __str__(self) -> str:
        return self.render()