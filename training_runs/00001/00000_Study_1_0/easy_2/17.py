def sat(s: str):
    return 'oo' in s and s.count('o') >= 1000

def sol():
    s = "The objective of the puzzle is to find a string 'oo' in the input and count at least 1000 'o' characters. The final checker will confirm that the solution is correct by running assert sat(sol())

print(sol())

if __name__ == "__main__":
    assert sat(sol())
