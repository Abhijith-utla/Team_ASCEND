def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return tuple(list(zip('dee', 'doo', 'dah!')))

# Test
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
