def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    result = []
    words = 'berlin berger linber linger gerber gerlin'.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            result.append(words[i] + words[j])
    return result

if __name__ == "__main__":
    assert sat(sol())
