from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text = TextNode("Anchor text", TextType.LINK, "boot.dev")
    html = HTMLNode("tag", "value", ["obj1", "obj2"], {"href": "https://www.google.com",
    "target": "_blank",})


    print(text)
    print(repr(html))

if __name__ == "__main__":
    main()