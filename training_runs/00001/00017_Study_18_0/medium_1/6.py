def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    ls = ['dog', 'cat', 'bird']
    if sat(ls):
        return 'dog'
    else:
        return 'not dog'

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
