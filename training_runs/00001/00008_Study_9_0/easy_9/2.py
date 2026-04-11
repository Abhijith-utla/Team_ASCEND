def sat(li: List[int]):
    return [chr(i) for i in li] == list("Python is fun".replace(" ", ""))

def sol():
    return [chr(i) for i in range(32, 127)]

if __name__ == "__main__":
    assert sat(sol())
