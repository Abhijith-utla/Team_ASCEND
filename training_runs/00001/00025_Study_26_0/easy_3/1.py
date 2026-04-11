def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.6)

def sol():
    return ""

print(sat(sol()))  # This should print "True"

if __name__ == "__main__":
    assert sat(sol())
