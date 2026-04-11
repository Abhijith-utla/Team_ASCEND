def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return [{'name': 'John', 'age': 28}, {'name': 'Alex', 'age': 32}, {'name': 'John', 'age': 29}, {'name': 'Alex', 'age': 34}]

if __name__ == "__main__":
    assert sat(sol())
