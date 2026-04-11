def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [[(i, j) for i in range(5) for j in range(5)] for _ in range(7)]

print(sol())

# The following code should pass the assertions in the given problem
# assert len(daygroups) == 7
# assert all(len(groups) == 5 and set(range(15)) == set({i for g in groups for i in g}) for groups in daygroups)
# assert all(len(g) == 5 for groups in daygroups for g in groups)
# assert len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

if __name__ == "__main__":
    assert sat(sol())
