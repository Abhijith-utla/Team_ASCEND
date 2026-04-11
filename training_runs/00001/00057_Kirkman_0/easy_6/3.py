def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in range(15) for i in (g for groups in daygroups for g in groups)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())
