def sat(answer):
    return tuple(answer) in zip('dee', 'doo', 'dah!')

def sol():
    return [i for i in 'dee' + 'doo' + 'dah!']

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
