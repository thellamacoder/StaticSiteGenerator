import unittest

from textnode import TextNode, TextType
from markdown_source import split_nodes_delimiter

class TestMarkdownToTextNodeList(unittest.TestCase):
	
	def test_inline_markdown_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_nodes, 
			[
			TextNode("This is text with a ", TextType.TEXT), 
			TextNode("code block", TextType.CODE), 
			TextNode(" word", TextType.TEXT)
			])

	def test_inline_markdown_bold(self):
		node = TextNode("This is *bold* text", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
		self.assertEqual(new_nodes, 
			[
			TextNode("This is ", TextType.TEXT),
			TextNode("bold", TextType.BOLD),
			TextNode(" text", TextType.TEXT)
        ])
	def test_inline_markdown_italic(self):
		node = TextNode("This is _italic_ text", TextType.TEXT)
		
		