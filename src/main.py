from textnode import TextNode, TextType
from markdown_source import *

def main():
	
	print("----")
	node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

	new_nodes = text_to_textnode(node)
	print(new_nodes)
	print("----")


main()
