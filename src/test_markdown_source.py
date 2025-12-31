import unittest

from textnode import TextNode, TextType
from markdown_source import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual(new_nodes,
			    [
				TextNode("This is ", TextType.TEXT),
	   			TextNode("italic", TextType.ITALIC),
				TextNode(" text", TextType.TEXT)
			    ])

	def test_extract_markdown_images1(self):
		matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_markdown_links1(self):
		matches = extract_markdown_links("This is text with links [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
		self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

	def test_split_images(self):
		node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
			],
			new_nodes,
		)
