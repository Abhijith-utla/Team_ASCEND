def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return [x for x in zip('dee', 'doo', 'dah!')]

if __name__ == "__main__":
    assert sat(sol())
