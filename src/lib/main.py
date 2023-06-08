import ast
python_code = """
a = b
v = d
"""

print(ast.dump(ast.parse(python_code)))
