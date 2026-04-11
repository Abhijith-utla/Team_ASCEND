def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

def sol():
    return "The answer is {}.".format(True)

if __name__ == "__main__":
    assert sat(sol())
