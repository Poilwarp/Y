vars = {}

def print_y(text, x, y):
    print(f"""{"\n" * y}
    {" " * x}{text}""")

def input_y(text, x, y):
    return input(f"""{"\n" * y}
    {" " * x}{text}""") 

def var(name, value):
    vars[name] = value 

fun = {"output": print_y, "input": input_y, "var": var}
