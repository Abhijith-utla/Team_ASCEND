def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    return [2, 1, 0]

assert sat(sol())
```

This code will return a list with the elements `[2, 1, 0]` as the output. The function `sat` checks if the given list is in the tuple `('dee', 'doo', 'dah!')`.

if __name__ == "__main__":
    assert sat(sol())
