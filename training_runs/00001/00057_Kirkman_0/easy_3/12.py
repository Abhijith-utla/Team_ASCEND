def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in g for g in groups) == set(range(1, 15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 64

def sol():
    return [
        [i for i in range(1, 15) if i not in (j for groups in daygroups for g in groups for j in g)],
        [i for groups in daygroups for i in (j for g in groups for j in g if i != j)]
    ]

print(sol())

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
