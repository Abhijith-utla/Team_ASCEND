def sat(li: List[str]):
    return all(len(i) <= 5 for i in li) and all(i.isalpha() for i in li)

def sol() -> str:
    li = []
    while True:
        s = input("Enter a string: ")
        if len(s) <= 5 and s.isalpha():
            li.append(s)
            if len(li) == 5:
                break
    return ' '.join(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
