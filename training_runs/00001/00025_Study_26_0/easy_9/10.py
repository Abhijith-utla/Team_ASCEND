def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    return [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9'
    ]

# To test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
