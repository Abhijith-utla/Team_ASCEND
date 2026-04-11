def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 4 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [[(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if a != b and a != c and a != d and b != c and b != d and c != d] for _ in range(7)]

# This will check the function 'sol' with the provided 'sat' function.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
