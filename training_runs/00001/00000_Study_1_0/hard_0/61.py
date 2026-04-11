def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    answer = ''
    for _ in range(1000):
        answer += 'oo'
    return answer

if __name__ == "__main__":
    assert sat(sol())
