def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

def sol():
    answer = ''
    for _ in range(400):
        answer += 'm'
    for _ in range(401):
        answer += 'mm'
    for _ in range(398):
        answer += 'mmm'
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
