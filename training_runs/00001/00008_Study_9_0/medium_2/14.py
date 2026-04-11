def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return [i for i in range(10)]

print(sat(sol()))  # Expected output: True

def sat(li: List[int]):
    return sorted(li) == li

print(sat(sol()))  # Expected output: True

def sat(li: List[int]):
    return len(set(li)) == len(li)

print(sat(sol()))  # Expected output: True

def sat(li: List[int]):
    return all(li[i] <= li[i+1] for i in range(len(li)-1)) and li[0] <= li[-1]

print(sat(sol()))  # Expected output: True

def sat(li: List[int]):
    return sum(li) == 55

print(sat(sol()))  # Expected output: True

def sat(li: List[int]):
    return len(li) == 5

print(sat(sol()))  # Expected output: True

def sat(li: List[int]

if __name__ == "__main__":
    assert sat(sol())
