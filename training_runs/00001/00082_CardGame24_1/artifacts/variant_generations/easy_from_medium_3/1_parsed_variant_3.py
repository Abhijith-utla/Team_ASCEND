def sat(expr):
    return eval(expr, {}, {"__builtins__" : None})

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
