def sat(x: List[int], s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    length = len(x)
    return all(s[x[i]] <= s[x[i + 1]] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
