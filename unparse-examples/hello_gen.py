#!/usr/bin/env python

import ast
from unparse import Unparser

# pretty-printing for easier inspection of ASTs
from ast_pprint import *

from os import linesep 


if __name__ == "__main__":
    
    # create AST (Abstract Syntax Tree)
    hello_str = ast.Str(s="hello world")
    print_stmt = ast.Print(dest=None, nl=True, values=[hello_str])
    my_ast = ast.Module(body=[print_stmt])
    print my_ast

    f = open("hello_out.py", "w")
    f.write("# AUTO-GENERATED FILE")
    f.write(linesep)

    # serialize AST to source code
    Unparser(my_ast, f)
    
    # write source code to file
    f.write(linesep)
    f.close()
