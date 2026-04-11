def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple('dee', 'doo', 'dah!')

if __name__ == "__main__":
    assert sat(sol())
