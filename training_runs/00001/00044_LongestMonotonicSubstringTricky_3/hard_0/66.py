def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

print(sat([], 61, " OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"))  # False
print(sat([0], 1, "O"))  # True
print(sat([0, 1], 2, "OI"))  # True
print(sat([0, 1, 2], 3, "OIA"))  # False
print(sat([2, 1, 0], 3, "RI"))  # True
print(sat([2, 0, 1], 3, "RO"))  # False
print(sat([1, 0, 2], 3, "RIO"))  # True
print(sat([2, 1, 0, 3], 4, "ROI"))  # False
print(sat([0, 2, 1, 3], 4, "OIU"))  # True
print(sat

if __name__ == "__main__":
    assert sat(sol())
