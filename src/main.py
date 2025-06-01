from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    text = TextNode("Anchor text", TextType.LINK, "boot.dev")
    html = HTMLNode("tag", "value", ["obj1", "obj2"], {"href": "https://www.google.com",
    "target": "_blank",})

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    node.to_html()


    print(text)
    print(repr(html))

    print(node.to_html())

if __name__ == "__main__":
    main()