def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(answer)

answer = ['d', 'e', 'o']
assert sat(answer)

if __name__ == "__main__":
    assert sat(sol())
