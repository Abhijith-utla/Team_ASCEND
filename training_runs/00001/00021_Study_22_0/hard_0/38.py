def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return ''.join(list(filter(lambda x: x % 2 == 0, sorted(list(set([x for x in range(10) if x % 2 == 0]))))))

print(sol())

#assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
