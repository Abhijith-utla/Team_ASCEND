def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    return x

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
