def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return {"answer": 'dah!'}

if __name__ == "__main__":
    assert sat(sol())
