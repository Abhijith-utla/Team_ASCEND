def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    def sat(x: float):
        return str(x - 3.1417).startswith("123.456")
    
    return sat

if __name__ == "__main__":
    assert sat(sol())
