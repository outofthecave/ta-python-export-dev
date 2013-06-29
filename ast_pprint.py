#!/usr/bin/env python

"""Add pretty-printing methods to classes from the `ast` module.

These methods are intended to ease inspection of ASTs. They do NOT 
serialize the AST to Python code. Instead, they visualize the AST in ASCII 
art.

The methods are added to the classes as `__str__` methods, so calling 
str(my_ast) is sufficient to use this module.
"""

import ast
from os import linesep


def _ast_node_to_string(node, indent=""):
    # buffer the string parts before joining them
    s = []

    # list or tuple of ASTs
    if (isinstance(node, (list, tuple)) and node and 
          isinstance(node[0], ast.AST)):
        
        s.append("[")
        s.append(linesep)
        
        leading_comma = False
        for item_ast in node:
            if leading_comma:
                s.append(indent)
                s.append(",")
                s.append(linesep)
            else:
                leading_comma = True
            s.append(indent + " ")
            s.append(_ast_node_to_string(item_ast, indent + " "))

        s.append(indent)
        s.append("]")
        s.append(linesep)
        
    # not an AST
    elif not isinstance(node, ast.AST):
        return repr(node) + linesep

    # AST
    else:
        s.append(type(node).__name__)
        s.append(linesep)
        
        for key, value in sorted(node.__dict__.iteritems()):
            if key not in ("lineno", "col_offset"):
                s.append(indent)
                s.append(str(key))
                s.append(" ")
                indent_new = indent + " " * (len(key) + 1)
                s.append(_ast_node_to_string(value, indent_new))
    
    return "".join(s)



ast.Add.__str__ = _ast_node_to_string
ast.And.__str__ = _ast_node_to_string
ast.Assert.__str__ = _ast_node_to_string
ast.Assign.__str__ = _ast_node_to_string
ast.Attribute.__str__ = _ast_node_to_string
ast.AugAssign.__str__ = _ast_node_to_string
ast.AugLoad.__str__ = _ast_node_to_string
ast.AugStore.__str__ = _ast_node_to_string
ast.BinOp.__str__ = _ast_node_to_string
ast.BitAnd.__str__ = _ast_node_to_string
ast.BitOr.__str__ = _ast_node_to_string
ast.BitXor.__str__ = _ast_node_to_string
ast.BoolOp.__str__ = _ast_node_to_string
ast.Break.__str__ = _ast_node_to_string
ast.Call.__str__ = _ast_node_to_string
ast.ClassDef.__str__ = _ast_node_to_string
ast.Compare.__str__ = _ast_node_to_string
ast.Continue.__str__ = _ast_node_to_string
ast.Del.__str__ = _ast_node_to_string
ast.Delete.__str__ = _ast_node_to_string
ast.Dict.__str__ = _ast_node_to_string
ast.DictComp.__str__ = _ast_node_to_string
ast.Div.__str__ = _ast_node_to_string
ast.Ellipsis.__str__ = _ast_node_to_string
ast.Eq.__str__ = _ast_node_to_string
ast.ExceptHandler.__str__ = _ast_node_to_string
ast.Exec.__str__ = _ast_node_to_string
ast.Expr.__str__ = _ast_node_to_string
ast.Expression.__str__ = _ast_node_to_string
ast.ExtSlice.__str__ = _ast_node_to_string
ast.FloorDiv.__str__ = _ast_node_to_string
ast.For.__str__ = _ast_node_to_string
ast.FunctionDef.__str__ = _ast_node_to_string
ast.GeneratorExp.__str__ = _ast_node_to_string
ast.Global.__str__ = _ast_node_to_string
ast.Gt.__str__ = _ast_node_to_string
ast.GtE.__str__ = _ast_node_to_string
ast.If.__str__ = _ast_node_to_string
ast.IfExp.__str__ = _ast_node_to_string
ast.Import.__str__ = _ast_node_to_string
ast.ImportFrom.__str__ = _ast_node_to_string
ast.In.__str__ = _ast_node_to_string
ast.Index.__str__ = _ast_node_to_string
ast.Interactive.__str__ = _ast_node_to_string
ast.Invert.__str__ = _ast_node_to_string
ast.Is.__str__ = _ast_node_to_string
ast.IsNot.__str__ = _ast_node_to_string
ast.LShift.__str__ = _ast_node_to_string
ast.Lambda.__str__ = _ast_node_to_string
ast.List.__str__ = _ast_node_to_string
ast.ListComp.__str__ = _ast_node_to_string
ast.Load.__str__ = _ast_node_to_string
ast.Lt.__str__ = _ast_node_to_string
ast.LtE.__str__ = _ast_node_to_string
ast.Mod.__str__ = _ast_node_to_string
ast.Module.__str__ = _ast_node_to_string
ast.Mult.__str__ = _ast_node_to_string
ast.Name.__str__ = _ast_node_to_string
ast.Not.__str__ = _ast_node_to_string
ast.NotEq.__str__ = _ast_node_to_string
ast.NotIn.__str__ = _ast_node_to_string
ast.Num.__str__ = _ast_node_to_string
ast.Or.__str__ = _ast_node_to_string
ast.Param.__str__ = _ast_node_to_string
ast.Pass.__str__ = _ast_node_to_string
ast.Pow.__str__ = _ast_node_to_string
ast.Print.__str__ = _ast_node_to_string
ast.RShift.__str__ = _ast_node_to_string
ast.Raise.__str__ = _ast_node_to_string
ast.Repr.__str__ = _ast_node_to_string
ast.Return.__str__ = _ast_node_to_string
ast.Set.__str__ = _ast_node_to_string
ast.SetComp.__str__ = _ast_node_to_string
ast.Slice.__str__ = _ast_node_to_string
ast.Store.__str__ = _ast_node_to_string
ast.Str.__str__ = _ast_node_to_string
ast.Sub.__str__ = _ast_node_to_string
ast.Subscript.__str__ = _ast_node_to_string
ast.Suite.__str__ = _ast_node_to_string
ast.TryExcept.__str__ = _ast_node_to_string
ast.TryFinally.__str__ = _ast_node_to_string
ast.Tuple.__str__ = _ast_node_to_string
ast.UAdd.__str__ = _ast_node_to_string
ast.USub.__str__ = _ast_node_to_string
ast.UnaryOp.__str__ = _ast_node_to_string
ast.While.__str__ = _ast_node_to_string
ast.With.__str__ = _ast_node_to_string
ast.Yield.__str__ = _ast_node_to_string

