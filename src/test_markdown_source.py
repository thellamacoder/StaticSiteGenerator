import unittest

from textnode import TextNode, TextType
from markdown_source import split_nodes_delimiter

class TestMarkdownToTextNodeList(unittest.TestCase):
	def test_inline_markdown(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_nodes, 
			[
			TextNode("This is text with a ", 
			TextType.TEXT), 
			TextNode("code block", TextType.CODE), 
			TextNode(" word", TextType.TEXT)
			])