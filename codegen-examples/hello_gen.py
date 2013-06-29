#!/usr/bin/env python

import ast
from codegen import to_source

# pretty-printing for easier inspection of ASTs
from ast_pprint import *

from os import linesep 


if __name__ == "__main__":
    
#     f_hand = open("hello_hand.py", "r")
#     source_hand = f_hand.read()
#     f_hand.close()
#     my_ast = ast.parse(source_hand)
#     print my_ast
    
    # create AST (Abstract Syntax Tree)
    hello_str = ast.Str(s="hello world")
    print_stmt = ast.Print(dest=None, nl=True, values=[hello_str])
    my_ast = ast.Module(body=[print_stmt])
    print my_ast

    # serialize AST to source code
    source_code = to_source(my_ast)
    
    # write source code to file
    f = open("hello_out.py", "w")
    f.write("# AUTO-GENERATED FILE")
    f.write(linesep)
    f.write(source_code)
    f.write(linesep)
    f.close()
