import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    #add more
    def test_repr(self):
        node = HTMLNode(
            "tag", "value", ["obj1", "obj2"], 
            {"href": "https://www.google.com", "target": "_blank",}
            )
        self.assertEqual(
            "HTMLNode(tag, value, ['obj1', 'obj2'], {'href': 'https://www.google.com', 'target': '_blank'})", 
            repr(node)
        )

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", ["obj1", "obj2"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())


if __name__ == "__main__":
    unittest.main()

    