def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    ls = input()
    ls = ls.split()
    return str(min(ls)) + " " + str(max(ls)) + " " + str(len(ls))

# Test cases
assert sat(["1", "2", "3", "4", "5"]) == False
assert sat(["1", "1", "1", "1", "1"]) == True
assert sat(["5", "5", "5", "5", "5"]) == True
assert sat(["1", "2", "3", "4"]) == False
assert sat(["1", "1", "2", "3"]) == True

if __name__ == "__main__":
    assert sat(sol())
