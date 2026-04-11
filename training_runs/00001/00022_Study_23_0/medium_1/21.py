def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return {
        'left_leg': 'doo',
        'right_leg': 'dee',
        'neck': 'dah!',
    }

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
