def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    answer = ""
    while len(answer) < 15:
        answer += "a"
        if len(answer) < 15:
            answer += "b"
        if len(answer) < 15:
            answer += "c"
        if len(answer) < 15:
            answer += "d"
        if len(answer) < 15:
            answer += "e"
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
