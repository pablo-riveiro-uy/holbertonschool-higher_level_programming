#!/usr/bin/python3
if __name__ == "__main__":
  import py_compile
  import ast
  with open(r'hidden_4.pyc') as file:
    node = ast.parse(file.read())
    def show_info(functionNode):
        function_rep = ''
        function_rep = functionNode.name + '('

        for arg in functionNode.args.args:
            function_rep += arg.arg + ','

        function_rep = function_rep.rstrip(function_rep[-1])
        function_rep += ')'
        return function_rep

result = []
functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

for function in functions:
    result.append(show_info(function))

for class_ in classes:
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        result.append((class_.name + '.' + show_info(method)))

print(', '.join(result))