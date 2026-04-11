def sat(ls: List[str]):
    return "".join(ls) == str(1234567890)

def sol():
    return [str(i) for i in range(10)]

# Output: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
