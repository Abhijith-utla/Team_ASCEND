def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(answer)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
