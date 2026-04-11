def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    ls = ["Python", "Java", "C++", "Ruby", "C#", "Go", "JavaScript", "PHP", "Perl", "Swift"]
    return sat(ls)

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

# The checker will pass if the function returns True
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
