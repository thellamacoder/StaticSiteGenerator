from textnode import TextNode, TextType
from markdown_source import *
from markdown_blocks import *

def main():
	
	print("----")
	md = """
# This is a heading

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
	
-This is a list
-with items"""
	print(markdown_to_blocks(md))
	print("----")




main()
