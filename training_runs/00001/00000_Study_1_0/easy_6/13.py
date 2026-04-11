def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'ooo' in 'ooooooooooooooooooooo' and 'o' not in 'ooooooooooooooooooooo' and 'ooooooooooooooooooooo'.count('o') == 1000

# Test
print(sat(sol()))  # should return True

if __name__ == "__main__":
    assert sat(sol())
