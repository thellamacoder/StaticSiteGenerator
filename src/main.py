from textnode import TextNode, TextType
from markdown_source import *

def main():

	print("TextNode(This is some anchor text, link, https://www.boot.dev)")

	node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
	new_nodes = split_nodes_image([node])
	print(new_nodes)


main()
