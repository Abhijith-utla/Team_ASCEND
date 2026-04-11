def sat(x: List[int], length=61):
    s = " OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"
    return all(s[x[i]] <= s[x[i + 1]] for i in range(length - 1))

def sol():
    answer = [13, 14, 15, 16, 17, 18]
    return answer

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
