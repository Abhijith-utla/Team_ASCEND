def sat(s: str):
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 3

def sol():
    answer = ""
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if str(8 ** 3).count(str(i) + str(j) + str(k)) > 8 and len(str(i) + str(j) + str(k)) == 3:
                    answer += str(i) + str(j) + str(k)
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
