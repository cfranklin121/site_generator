class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        #match (self.props)
        #case TEXT
        #case BOLD
        #case ITALIC
        #case CODE
        #case LINK
        new_str = ""
        for key, value in self.props.items():
            new_str = new_str + f' {key}="{value}"'
        return new_str
    
        #case IMAGE
        #case _:

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"