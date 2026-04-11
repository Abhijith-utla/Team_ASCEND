def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    def is_power_of_eight(n: str):
        return n.count('8') > 8 and len(n) == 3

    def count_substring(s: str, sub: str):
        return s.count(sub)

    eight_powers = [str(8 ** i) for i in range(2888)]
    answer = ''

    for power in eight_powers:
        if is_power_of_eight(power):
            answer += power

    for i in range(len(answer) - 2):
        if answer[i] == '8' and answer[i + 1] == '8' and answer[i + 2] == '8':
            answer = answer[:i] + '0' + answer[i + 2:]

    for i in range(len(answer) - 2, -1, -1):
        if answer[i] == '8' and answer[i + 1] == '8' and answer[i + 2] == '8':
            answer = answer[:i] + '0'

if __name__ == "__main__":
    assert sat(sol())
