def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    import math
    answer = (8 ** 2888) ** 0.5
    answer_str = str(answer)
    return answer_str.count('0') + answer_str.count('1') + answer_str.count('2') + answer_str.count('3') + answer_str.count('4') + answer_str.count('5') + answer_str.count('6') + answer_str.count('7') + answer_str.count('8') + answer_str.count('9') > 8

if __name__ == "__main__":
    assert sat(sol())
