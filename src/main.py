from textnode import TextNode, TextType
from markdown_source import *
from markdown_blocks import *
import os
import shutil

def main():
 
    pass



def setup_site():
    
    public = os.path.exists("public")
    if public:
       print("the public file exists")
       shutil.rmtree("public/")
       os.mkdir("public")
    else:
        print("that folder does not exist")
        print(os.listdir())
    # clear public

    # find contents of source

    # copy contents of source into public

    

main()
setup_site()