def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    answer = sat('oo' * 1000)
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
