def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 4 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [{i for i in range(1, 16)}, {j for j in range(1, 16)}, {i, j} for j in range(1, 16)] for i in range(1, 16)
    ]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
