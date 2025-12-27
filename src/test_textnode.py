import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.TEXT)
		self.assertEqual(node, node2)
	
	def test_eq_false(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertNotEqual(node, node2)

	def test_eq_url(self):
		node = TextNode("Here is a URL", TextType.TEXT, "https://boot.dev")
		node2 = TextNode("Here is a URL", TextType.TEXT, "https://boot.dev")

	def test_eq_false_text(self):
		node = TextNode("I am groot!", TextType.IMAGE)
		node2 = TextNode("I am not groot!", TextType.IMAGE)

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_text_bold(self):
		node = TextNode("Here is some bold text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "Here is some bold text")

	def test_text_italic(self):
		node = TextNode("Here is some italic text", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "Here is some italic text")

	def test_text_code(self):
		node = TextNode("Here is code", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "Here is code")

	def test_text_link(self):
		node = TextNode("Link to google", TextType.LINK, "www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.value, "Link to google")


if __name__ == "__main__":
	unittest.main()
