def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return [{
        "word": "apple",
        "count": 2
    }, {
        "word": "banana",
        "count": 1
    }]

if __name__ == "__main__":
    assert sat(sol())
