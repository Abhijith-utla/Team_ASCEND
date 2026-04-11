def sat(li: List[int]):
    return [chr(i) for i in li] == list("Hello World".replace(" ", ""))

def sol():
    return [chr(i) for i in [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
