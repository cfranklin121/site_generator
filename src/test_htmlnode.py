import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_value(self):
        node = HTMLNode("test", "test2")
        node2 = HTMLNode("test", "test2")
        self.assertEqual(node.tag, "test")

    def test_value2(self):
        node = HTMLNode("test", "test2")
        node2 = HTMLNode("test", "test2")
        self.assertEqual(node.value, "test2")

    def test_None(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node.tag, node2.tag)

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

    #LeafNodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    #ParentNodes
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

            
            self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()

    