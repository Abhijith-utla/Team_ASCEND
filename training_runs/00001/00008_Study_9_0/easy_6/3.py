def sat(li: List[str]):
    return all(len(i) <= 5 for i in li) and all(i.isalpha() for i in li)

def sol():
    li = ["hello", "world", "pytho", "test"]
    assert sat(li)
    return None

if __name__ == "__main__":
    assert sat(sol())
