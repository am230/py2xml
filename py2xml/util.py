import typing as t
from xml.etree import ElementTree
from .element import Element
from strbuilder import Builder, SurroundBuilder
import keyword


def from_xml(tree: ElementTree.Element, target: t.Optional[Element] = None, factory: t.Optional[t.Callable[[str], Element]] = Element):
    target = target or factory(tree.tag)

    return target(**tree.attrib)[tree.text, *(from_xml(child, factory=factory) for child in tree)]


def from_xml_str(string: str, target: t.Optional[Element] = None, factory: t.Optional[t.Callable[[str], Element]] = Element):
    return from_xml(ElementTree.fromstring(string), target=target, factory=factory)


def is_tree_not_empty(tree: ElementTree.Element):
    return any(True for _ in tree)


def _format_value(value: str):
    if '\n' in value:
        return '"""%s"""' % value.replace('"', '\\"')
    return '"%s"' % value.replace('"', '\\"')


def _generate_code(tree: ElementTree.Element, elements=None) -> str:
    if elements is None:
        elements = {}
    tag = tree.tag
    if tag not in elements:
        if keyword.iskeyword(tag) or not tag.isascii():
            name = ''.join(filter(str.isascii, tag))
            i = 0
            values = elements.values()
            while name + str(i) in values:
                i += 1
            elements[tag] = name + str(i)
        else:
            elements[tag] = tag
    return (
        Builder(elements[tree.tag], separator='')
        .write_if(tree.attrib, lambda: f"({', '.join(f'{key}={_format_value(value)}' for key, value in tree.attrib.items())})")
        .write_if(tree.text or is_tree_not_empty(tree),
                  lambda: SurroundBuilder(surround=['[\n', '\n]'], separator=',\n')
                  .write_if(tree.text.strip(), lambda: _format_value(tree.text))
                  .write_if(is_tree_not_empty(tree), lambda: (_generate_code(child, elements) for child in tree))
                  )
    ).build()


def generate_code(tree: t.Union[ElementTree.Element, str]) -> str:
    if isinstance(tree, str):
        tree = ElementTree.fromstring(tree)
    elements = {}
    code = _generate_code(tree, elements=elements)
    return '\n'.join(f'{value} = py2xml.Element("{key}")' for key, value in elements.items()) + '\n' + code
