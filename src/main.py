from textnode import TextNode, TextType
from markdown_source import *

def main():

	node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
	new_nodes = split_nodes_image([node])
	print(new_nodes)

	node = TextNode("This is _italic_ text", TextType.TEXT)
	new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
	print(new_nodes)


main()
