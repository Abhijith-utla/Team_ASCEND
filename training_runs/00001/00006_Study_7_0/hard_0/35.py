def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    answer = ''
    for _ in range(8 ** 2888):
        answer += '8'
    answer = answer[:3]
    return answer

if __name__ == "__main__":
    assert sat(sol())
