from xml.etree import ElementTree
import py2xml


# generate code
print(py2xml.util.generate_code(ElementTree.fromstring('''<messages>
  <note id="501">
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
  <note id="502">
    <to>Jani</to>
    <from>Tove</from>
    <heading>Re: Reminder</heading>
    <body>I will not</body>
  </note>
</messages>''')))


# typing attributes
@py2xml.to_element
def note(id: int): ...


messages = py2xml.Element("messages")
to = py2xml.Element("to")
from0 = py2xml.Element("from")
heading = py2xml.Element("heading")
body = py2xml.Element("body")
print(
    messages[
        note(id=501)[
            to[
                "Tove"
            ],
            from0[
                "Jani"
            ],
            heading[
                "Reminder"
            ],
            body[
                "Don't forget me this weekend!"
            ]
        ],
        note(id=502)[
            to[
                "Jani"
            ],
            from0[
                "Tove"
            ],
            heading[
                "Re: Reminder"
            ],
            body[
                "I will not"
            ]
        ]
    ]
)