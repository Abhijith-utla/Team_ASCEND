def sat(li: List[int]):
    return [chr(i) for i in li] == list("Hello World".replace(" ", ""))

def sol():
    return [chr(i) for i in range(ord('a'), ord('z')+1)]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
