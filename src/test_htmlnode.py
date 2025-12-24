import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("<a>", "Hello World!", None, {"href": "https://www.google.com", "target": "_blank"},)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("a", "Hello World!", None, {"href": "https://www.google.com"},)
        self.assertEqual(node.__repr__(), "HTMLNode(Tag: a, Value: Hello World!, Children: None, Props: {'href': 'https://www.google.com'})")


    def test_values(self):
         node = HTMLNode("div", "I'm happy!")

         self.assertEqual(node.tag, "div")

         self.assertEqual(node.value, "I'm happy!")
         
         self.assertEqual(node.children, None)
         
         self.assertEqual(node.props, None)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!", None)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here")
        self.assertEqual(node.to_html(), "<a>Click here</a>")

    def test_leaf_to_html_a_link(self):
        node = LeafNode("a", "Click here", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Click here</a>')

class TestParentNode(unittest.TestCase):
     
    def test_parentnode_one_child(self):
        child_node = LeafNode("i", "italic text")
        node = ParentNode("p", [child_node], None)
        self.assertEqual(node.to_html(), "<p><i>italic text</i></p>")

    def test_parentnode_two_children(self):
        child_node1 = LeafNode("b", "bold text")
        child_node2 = LeafNode("i", "italic text")
        node = ParentNode("p",[child_node1, child_node2], None)
        self.assertEqual(node.to_html(), "<p><b>bold text</b><i>italic text</i></p>")

    def test_two_parentnode_one_child(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        node = ParentNode("div", [child_node])
        self.assertEqual(node.to_html(), "<div><span><b>grandchild</b></span></div>")


if __name__ == "__main__":
	unittest.main()