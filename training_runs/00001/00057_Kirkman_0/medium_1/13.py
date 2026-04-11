def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [3, 2, 1, 0, 3],
        [4, 1, 2, 0, 4],
        [5, 2, 3, 0, 5],
        [6, 3, 4, 0, 6],
        [5, 4, 5, 0, 5],
        [6, 5, 6, 0, 6],
        [7, 6, 7, 0, 7]
    ]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
