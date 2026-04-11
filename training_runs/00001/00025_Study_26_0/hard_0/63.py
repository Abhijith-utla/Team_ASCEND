def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return [str(int(i)) * 8 for i in range(8)]

# Testing the function
print(sat(sol()))  # Expected output: False

if __name__ == "__main__":
    assert sat(sol())
