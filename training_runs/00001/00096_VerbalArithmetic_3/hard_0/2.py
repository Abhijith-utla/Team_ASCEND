def sat(li: List[int], words=['fqjb', 'awqw', 'lfll', 'fvvvb']):
    assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
    assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
    return sum(li[:-1]) == li[-1]

def sol():
    li = [1, 2, 3, 4, 5]
    words = ['fqjb', 'awqw', 'lfll', 'fvvvb']
    assert sat(li, words)
    return sum(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
