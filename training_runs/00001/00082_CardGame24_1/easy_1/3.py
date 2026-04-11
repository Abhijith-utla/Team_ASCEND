def sat(expr):
    if eval(expr) == 24:
        return True
    else:
        return False

def sol():
    return "4*6"

if __name__ == "__main__":
    assert sat(sol())
