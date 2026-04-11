def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return {
        'dee': 'doo',
        'dah!': 'ha!'
    }

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
