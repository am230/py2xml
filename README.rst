Writing XML with Pythonic code
==============================

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: http://opensource.org/licenses/MIT
.. image:: https://badge.fury.io/py/py2xml.svg
    :target: https://badge.fury.io/py/py2xml

Installation
------------

.. code:: bash

    $ pip install py2xml

Usage
-------

.. code:: python

    import py2xml

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


<messages><note id="501"><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note><note id="502"><to>Jani</to><from>Tove</from><heading>Re: Reminder</heading><body>I will not</body></note></messages>

to xml ElementTree
------------------

.. code:: python

    Element.to_xml()

generate code
-------------

.. code:: python

    import py2xml

    print(py2xml.util.generate_code('''<messages>
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
    </messages>'''))


.. code:: python

    messages = py2xml.Element("messages")
    note = py2xml.Element("note")
    to = py2xml.Element("to")
    from0 = py2xml.Element("from")
    heading = py2xml.Element("heading")
    body = py2xml.Element("body")
    messages[
    note(id="501")[
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
    note(id="502")[
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
