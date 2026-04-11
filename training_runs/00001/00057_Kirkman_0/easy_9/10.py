def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 5 for g in daygroups for groups in daygroups)
    return len({(i, j) for g in daygroups for groups in daygroups for i in g for j in g}) == 16

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
