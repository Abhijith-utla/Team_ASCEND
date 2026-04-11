def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s)

def sol():
    return "This string is not acceptable because it's longer than 30 characters or less than 5 characters."

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
