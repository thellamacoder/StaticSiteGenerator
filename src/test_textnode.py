import unittest

from textnode import TextNode, TextType

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
		node = TextNode("Here is a URL", TextType.LINK, "https://boot.dev")
		node2 = TextNode("Here is a URL", TextType.LINK, "https://boot.dev")

	def test_eq_false_text(self):
		node = TextNode("I am groot!", TextType.IMAGE)
		node2 = TextNode("I am not groot!", TextType.IMAGE)

if __name__ == "__main__":
	unittest.main()
