def sat(li: List[int]):
    return [chr(i) for i in li] == list("Python is fun".replace(" ", ""))

def sol():
    return ''.join(chr(i) for i in range(97, 123))

print(sat(list(map(ord, 'python is fun'))))

if __name__ == "__main__":
    assert sat(sol())
