def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return [{"name": "John", "age": 30}, {"name": "Jane", "age": 28}, {"name": "Joe", "age": 32}]

if __name__ == "__main__":
    assert sat(sol())
