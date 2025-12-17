import unittest

from htmlnode import HTMLNode

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



if __name__ == "__main__":
	unittest.main()