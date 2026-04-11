def sat(s: str):
    return 'oo' in s and s.count('o') <= 1000

def sol():
    return 'oo' in 'Hello, world!' and 'Hello, world!'.count('o') <= 1000

# To validate the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
