def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s)

def sol():
    s = input()
    if sat(s):
        return {"answer": "Yes"}
    else:
        return {"answer": "No"}

def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s)

# Testing the solution
assert sol() == {"answer": "No"}
assert sol("This is a very long string") == {"answer": "Yes"}
assert sol("short") == {"answer": "No"}

if __name__ == "__main__":
    assert sat(sol())
