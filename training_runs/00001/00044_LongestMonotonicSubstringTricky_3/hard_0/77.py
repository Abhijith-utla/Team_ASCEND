def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

print(sat())
print(sat([0, 1, 2, 3, 4]))
print(sat([4, 3, 2, 1, 0]))
print(sat([0, 1, 2, 3]))
print(sat([4, 3, 5, 6, 7]))
print(sat([5, 4, 3, 2, 1, 0]))
print(sat([5, 6, 7, 4, 3, 2, 1, 0]))

if __name__ == "__main__":
    assert sat(sol())
