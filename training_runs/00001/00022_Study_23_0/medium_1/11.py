def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(answer)

def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

answer = sol()
assert sat(answer)

if __name__ == "__main__":
    assert sat(sol())
